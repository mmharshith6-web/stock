import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import warnings
import json
warnings.filterwarnings('ignore')

class StockPredictor:
    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None
        self.lookback = 60
        
    def prepare_data(self, data, lookback=60):
        """Prepare data for LSTM model"""
        scaled_data = self.scaler.fit_transform(data.reshape(-1, 1))
        
        X, y = [], []
        for i in range(lookback, len(scaled_data)):
            X.append(scaled_data[i-lookback:i, 0])
            y.append(scaled_data[i, 0])
            
        return np.array(X), np.array(y)
    
    def build_model(self, input_shape):
        """Build LSTM model for stock prediction"""
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
        model.add(Dropout(0.2))
        
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        
        model.add(Dense(units=1))
        
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
    
    def train(self, training_data, epochs=5, batch_size=32):  # Reduced epochs for faster execution
        """Train the LSTM model"""
        # Prepare data
        X_train, y_train = self.prepare_data(training_data)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        
        # Build model
        self.model = self.build_model((X_train.shape[1], 1))
        
        # Train model
        history = self.model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            verbose=0
        )
        
        return history
    
    def predict(self, data, lookback=60):
        """Make predictions using the trained model"""
        if self.model is None:
            raise ValueError("Model not trained yet. Call train() first.")
            
        # Scale the data
        scaled_data = self.scaler.transform(data.reshape(-1, 1))
        
        # Prepare test data
        X_test = []
        for i in range(lookback, len(scaled_data)):
            X_test.append(scaled_data[i-lookback:i, 0])
            
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        
        # Make predictions
        predictions = self.model.predict(X_test, verbose=0)
        predictions = self.scaler.inverse_transform(predictions)
        
        return predictions
    
    def create_future_predictions(self, data, days=30):
        """Predict future stock prices"""
        if self.model is None:
            raise ValueError("Model not trained yet. Call train() first.")
            
        # Get the last 60 days of data
        last_sequence = data[-60:]
        future_predictions = []
        
        current_sequence = last_sequence.reshape(-1, 1)
        current_sequence_scaled = self.scaler.transform(current_sequence)
        
        for _ in range(days):
            # Prepare input
            X = current_sequence_scaled[-60:].reshape(1, 60, 1)
            
            # Predict next value
            next_pred_scaled = self.model.predict(X, verbose=0)
            next_pred = self.scaler.inverse_transform(next_pred_scaled)
            future_predictions.append(float(next_pred[0, 0]))  # Convert to float
            
            # Update sequence for next prediction
            next_value_scaled = next_pred_scaled[0, 0]
            current_sequence_scaled = np.append(current_sequence_scaled, next_value_scaled)
            
        return future_predictions

def load_sample_data():
    """Create sample stock data for demonstration"""
    # Generate sample data similar to Google stock prices
    np.random.seed(42)
    dates = pd.date_range('2020-01-01', periods=100, freq='D')  # Reduced data points
    
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

def save_model(predictor, filepath):
    """Save model weights and scaler parameters"""
    model_data = {
        'scaler_min': predictor.scaler.min_.tolist(),
        'scaler_scale': predictor.scaler.scale_.tolist(),
        'lookback': predictor.lookback
    }
    
    # Save model weights
    predictor.model.save_weights(filepath + '_weights.h5')
    
    # Save scaler and other parameters
    with open(filepath + '_params.json', 'w') as f:
        json.dump(model_data, f)

def load_model(filepath):
    """Load model weights and scaler parameters"""
    # Load parameters
    with open(filepath + '_params.json', 'r') as f:
        model_data = json.load(f)
    
    # Create new predictor
    predictor = StockPredictor()
    predictor.lookback = model_data['lookback']
    
    # Set scaler parameters
    predictor.scaler.min_ = np.array(model_data['scaler_min'])
    predictor.scaler.scale_ = np.array(model_data['scaler_scale'])
    
    # Build model and load weights
    predictor.model = predictor.build_model((predictor.lookback, 1))
    predictor.model.load_weights(filepath + '_weights.h5')
    
    return predictor

if __name__ == "__main__":
    # Load data
    df = load_sample_data()
    print(f"Generated sample data with {len(df)} records")
    print(df.head())
    
    # Initialize predictor
    predictor = StockPredictor()
    
    # Train model
    training_data = df['Close'].values
    print("Training model...")
    history = predictor.train(training_data, epochs=5)  # Further reduced epochs
    print("Model training completed!")
    
    # Make predictions
    predictions = predictor.predict(training_data)
    print(f"Generated {len(predictions)} predictions")
    
    # Save model and data for web app
    save_model(predictor, 'stock_predictor_model')
    df.to_csv('sample_stock_data.csv', index=False)
    print("Model and data saved successfully!")