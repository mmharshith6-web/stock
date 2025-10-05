from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import os
import requests
from datetime import datetime, timedelta

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

# Global variables for data
stock_data = {}

# Alpha Vantage API key (you would need to get your own free API key from https://www.alphavantage.co/support/#api-key)
ALPHA_VANTAGE_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key

def fetch_real_stock_data(symbol):
    """Fetch real stock data from Alpha Vantage API"""
    try:
        # Use TIME_SERIES_DAILY endpoint to get daily stock prices
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact"
        response = requests.get(url)
        data = response.json()
        
        # Check if we got valid data
        if "Time Series (Daily)" not in data:
            print(f"Error fetching data for {symbol}: {data}")
            return None
            
        # Extract time series data
        time_series = data["Time Series (Daily)"]
        
        # Convert to DataFrame
        df_data = []
        for date, values in time_series.items():
            df_data.append({
                'Date': date,
                'Open': float(values['1. open']),
                'High': float(values['2. high']),
                'Low': float(values['3. low']),
                'Close': float(values['4. close']),
                'Volume': int(values['5. volume'])
            })
        
        # Create DataFrame and sort by date
        df = pd.DataFrame(df_data)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date').reset_index(drop=True)
        
        return df
    except Exception as e:
        print(f"Error fetching real stock data for {symbol}: {e}")
        return None

def load_sample_data():
    """Create sample stock data for demonstration"""
    # Generate sample data similar to Google stock prices
    np.random.seed(42)
    dates = pd.date_range(datetime.now() - timedelta(days=100), periods=100, freq='D')
    
    # Simulate stock price movement
    prices = [1000]  # Starting price
    for i in range(1, 100):
        change = np.random.normal(0, 2)  # Random change
        new_price = prices[-1] * (1 + change/100)
        prices.append(float(max(new_price, 0.01)))  # Ensure positive prices and convert to float
    
    df = pd.DataFrame({
        'Date': dates,
        'Open': [float(p) for p in prices],
        'High': [float(p * (1 + abs(np.random.normal(0, 1))/100)) for p in prices],
        'Low': [float(p * (1 - abs(np.random.normal(0, 1))/100)) for p in prices],
        'Close': [float(p * (1 + np.random.normal(0, 0.5)/100)) for p in prices],
        'Volume': [int(np.random.randint(1000000, 10000000)) for _ in range(100)]
    })
    
    return df

def get_stock_data(symbol):
    """Get stock data for a symbol, fetching real data if API key is provided"""
    global stock_data
    
    # If we already have data for this symbol, return it
    if symbol in stock_data:
        return stock_data[symbol]
    
    # If we have a valid API key, try to fetch real data
    if ALPHA_VANTAGE_API_KEY != "YOUR_API_KEY_HERE" and ALPHA_VANTAGE_API_KEY:
        df = fetch_real_stock_data(symbol)
        if df is not None:
            stock_data[symbol] = df
            return df
    
    # Otherwise, return sample data
    df = load_sample_data()
    stock_data[symbol] = df
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get parameters from request
        data = request.get_json()
        days = data.get('days', 30) if data else 30
        symbol = data.get('symbol', 'GOOGL') if data else 'GOOGL'
        
        # Get stock data
        df = get_stock_data(symbol)
        
        # Generate simulated future predictions
        last_price = df['Close'].iloc[-1]
        future_predictions = []
        
        # Simulate future prices with random walk
        current_price = last_price
        for _ in range(days):
            change = np.random.normal(0, 2)  # Random change
            current_price = current_price * (1 + change/100)
            future_predictions.append(float(max(current_price, 0.01)))
        
        # Create future dates
        last_date = df['Date'].iloc[-1]
        future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days, freq='D')
        
        # Format response
        predictions = []
        for i in range(len(future_dates)):
            predictions.append({
                'date': future_dates[i].strftime('%Y-%m-%d'),
                'price': float(future_predictions[i])
            })
        
        return jsonify({
            'success': True,
            'symbol': symbol,
            'predictions': predictions
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/historical')
def historical():
    try:
        # Get symbol from query parameters or default to GOOGL
        symbol = request.args.get('symbol', 'GOOGL')
        
        # Get stock data
        df = get_stock_data(symbol)
        
        # Get last 100 data points for display
        recent_data = df.tail(100)
        
        historical_data = []
        for _, row in recent_data.iterrows():
            historical_data.append({
                'date': row['Date'].strftime('%Y-%m-%d'),
                'open': float(row['Open']),
                'high': float(row['High']),
                'low': float(row['Low']),
                'close': float(row['Close']),
                'volume': int(row['Volume'])
            })
        
        return jsonify({
            'success': True,
            'symbol': symbol,
            'data': historical_data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)