# Deployment Instructions for Stock Price Prediction Project

## Project Overview
This is a machine learning-based stock price prediction application with a futuristic UI. The application uses LSTM neural networks to predict stock prices and provides a responsive web interface for visualization.

## Prerequisites
- Git installed on your system
- GitHub account
- Python 3.8 or higher

## Local Setup

1. The project is already initialized as a Git repository with all files committed.
2. To verify the current status, run:
   ```bash
   git status
   ```

## Pushing to GitHub

### If the repository already exists on GitHub:

1. Add your GitHub repository as remote:
   ```bash
   git remote add origin https://github.com/mmharshith6-web/stock.git
   ```

2. Push the code to GitHub:
   ```bash
   git push -u origin master
   ```

### If you encounter authentication issues:

1. **Using HTTPS (username/password)**:
   ```bash
   git remote set-url origin https://github.com/mmharshith6-web/stock.git
   git push -u origin master
   ```
   When prompted, enter your GitHub username and personal access token (not password).

2. **Using SSH (SSH keys)**:
   ```bash
   git remote set-url origin git@github.com:mmharshith6-web/stock.git
   git push -u origin master
   ```
   Make sure you have SSH keys set up with GitHub.

### If the repository doesn't exist on GitHub:

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name your repository "stock"
   - Choose Public or Private
   - Don't initialize with a README
   - Click "Create repository"

2. Add the remote and push:
   ```bash
   git remote add origin https://github.com/mmharshith6-web/stock.git
   git branch -M main
   git push -u origin main
   ```

## Running the Application

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to http://localhost:5000

## Features

- Real-time stock data visualization
- LSTM-based price prediction
- Responsive and futuristic UI with animations
- Developer information section
- Multiple stock symbol support

## Developer Information

- **Name**: Harshith
- **Email**: mmharshith6@gmail.com
- **Phone**: 7411801829
- **GitHub**: https://github.com/mmharshith6-web
- **LinkedIn**: https://www.linkedin.com/in/mmcodes/
- **Portfolio**: https://portfolio2-mu-puce.vercel.app/

## Technologies Used

- Python
- Flask (Backend)
- HTML/CSS/JavaScript (Frontend)
- Chart.js (Data Visualization)
- TensorFlow/Keras (Machine Learning)
- Pandas/Numpy (Data Processing)

## Troubleshooting

### Authentication Issues
If you're having trouble pushing to GitHub, you may need to:

1. **Create a Personal Access Token**:
   - Go to GitHub Settings > Developer settings > Personal access tokens
   - Generate a new token with "repo" permissions
   - Use this token instead of your password when prompted

2. **Set up SSH Keys** (recommended for frequent pushes):
   - Generate an SSH key: `ssh-keygen -t rsa -b 4096 -C "mmharshith6@gmail.com"`
   - Add the key to your SSH agent
   - Add the public key to your GitHub account (Settings > SSH and GPG keys)

### Common Git Commands

- Check remote URLs: `git remote -v`
- Change remote URL: `git remote set-url origin <new-url>`
- Check branch status: `git branch -a`
- Create and switch to main branch: `git checkout -b main`

## License

This project is for educational purposes only.