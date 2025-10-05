# Stock Price Prediction Project

## Overview
This is a machine learning-based stock price prediction application with a futuristic UI. The application uses LSTM neural networks to predict stock prices and provides a responsive web interface for visualization.

## Features
- Real-time stock data visualization
- LSTM-based price prediction
- Responsive and futuristic UI with animations
- Developer information section
- Multiple stock symbol support

## Technologies Used
- Python
- Flask (Backend)
- HTML/CSS/JavaScript (Frontend)
- Chart.js (Data Visualization)
- Pandas/Numpy (Data Processing)

## Deployment on Vercel

### Prerequisites
1. A Vercel account (https://vercel.com)
2. This repository pushed to GitHub/GitLab/Bitbucket

### Deployment Steps
1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Import this repository
4. Configure the project:
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: ` `
   - Install Command: ` `
5. Add Environment Variables (if using real stock data):
   - `ALPHA_VANTAGE_API_KEY` - Your Alpha Vantage API key
6. Click "Deploy"

### Environment Variables
To use real stock data instead of sample data:
1. Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Add it as an environment variable in your Vercel project settings:
   - Key: `ALPHA_VANTAGE_API_KEY`
   - Value: Your API key

## Local Development

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-price-prediction
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to http://localhost:5000

## Project Structure
```
├── app.py                 # Flask application
├── stock_predictor.py     # Stock prediction model
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── .gitignore            # Git ignore file
├── templates/            # HTML templates
│   └── index.html        # Main application page
├── static/               # Static assets (if any)
└── README.md             # This file
```

## Developer Information
- **Name**: Harshith
- **Email**: mmharshith6@gmail.com
- **Phone**: 7411801829
- **GitHub**: https://github.com/mmharshith6-web
- **LinkedIn**: https://www.linkedin.com/in/mmcodes/
- **Portfolio**: https://portfolio2-mu-puce.vercel.app/

## License
This project is for educational purposes only.