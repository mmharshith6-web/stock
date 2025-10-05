import pandas as pd
import numpy as np
from stock_predictor import StockPredictor, load_model

# Load the sample data
df = pd.read_csv('sample_stock_data.csv')
print(f"Loaded data with {len(df)} records")

# Load the model
try:
    predictor = load_model('stock_predictor_model')
    print("Model loaded successfully!")
    
    # Test prediction
    closing_prices = df['Close'].values
    predictions = predictor.create_future_predictions(closing_prices, 5)
    print(f"Generated {len(predictions)} predictions:")
    for i, pred in enumerate(predictions):
        print(f"  Day {i+1}: ${pred:.2f}")
        
except Exception as e:
    print(f"Error loading model: {e}")