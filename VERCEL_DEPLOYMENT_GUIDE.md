# Vercel Deployment Guide for Stock Price Prediction App

## Overview
This guide will help you deploy the Stock Price Prediction application to Vercel. The application is built with Flask and uses Python for the backend.

## Prerequisites
1. A GitHub account with the repository pushed
2. A Vercel account (https://vercel.com/signup)
3. (Optional) Alpha Vantage API key for real stock data

## Deployment Steps

### 1. Prepare Your Repository
Make sure your repository includes the following files:
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel configuration
- `templates/` - HTML templates directory
- `.gitignore` - Git ignore file

### 2. Import Project to Vercel
1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Import your GitHub repository
4. Vercel should automatically detect this is a Python project

### 3. Configure Project Settings
In the "Configure Project" section:

**Build and Output Settings:**
- Framework Preset: Other
- Build Command: `pip install -r requirements.txt`
- Output Directory: Leave empty
- Install Command: Leave empty

**Environment Variables (Optional):**
If you want to use real stock data:
1. Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Add it as an environment variable:
   - Key: `ALPHA_VANTAGE_API_KEY`
   - Value: Your API key

### 4. Deploy
1. Click "Deploy"
2. Wait for the build process to complete (this may take several minutes)
3. Once deployed, Vercel will provide you with a URL to access your application

## Troubleshooting Common Issues

### 1. Build Failures
If your build fails, check the build logs for specific error messages:
- Ensure all dependencies in `requirements.txt` are correct
- Check that `vercel.json` is properly formatted
- Verify that `app.py` exports the Flask app as `app`

### 2. Runtime Errors
If the application deploys but doesn't work:
- Check the function logs in Vercel dashboard
- Ensure environment variables are set correctly
- Verify that file paths in `app.py` are correct

### 3. Large File Issues
Vercel has limits on deployment size:
- If you have large model files (.pkl, .h5), consider:
  1. Removing them and using sample data only
  2. Loading models from external storage
  3. Using smaller models

### 4. Python Version Issues
Vercel supports specific Python versions:
- Currently supports Python 3.6 through 3.9
- Ensure your dependencies are compatible with these versions
- Specify the Python version in `vercel.json` if needed

## Vercel Configuration Explained

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python",
      "config": {
        "runtime": "python3.9",
        "includeFiles": [
          "templates/**",
          "static/**",
          "*.py",
          "*.txt",
          "*.csv"
        ]
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "FLASK_APP": "app.py",
    "FLASK_ENV": "production"
  }
}
```

### Key Configuration Points:
1. **builds**: Defines how Vercel should build your application
2. **src**: Entry point for your application
3. **use**: Specifies the Vercel builder to use
4. **config**: Additional build configuration
5. **routes**: URL routing configuration
6. **env**: Environment variables for the application

## Optimizing for Vercel

### 1. Reduce Dependencies
Only include necessary packages in `requirements.txt`:
```
flask==2.0.3
numpy==1.21.6
pandas==1.3.5
requests==2.27.1
```

### 2. Optimize File Sizes
- Remove large model files if possible
- Compress static assets
- Use efficient data formats

### 3. Environment Variables
Use environment variables for:
- API keys
- Configuration settings
- Feature flags

## Monitoring and Logs

### Accessing Logs
1. Go to your project in Vercel dashboard
2. Click on "Functions" tab
3. View logs for specific deployments

### Performance Monitoring
- Vercel provides built-in performance metrics
- Monitor response times and error rates
- Set up alerts for critical issues

## Updating Your Deployment

### Automatic Deployments
- Vercel automatically deploys new commits to the main branch
- You can configure which branches trigger deployments

### Manual Deployments
1. Go to your project in Vercel dashboard
2. Click "Deployments" tab
3. Click "Redeploy" for a previous deployment
4. Or create a new deployment from the latest code

## Developer Information
- **Name**: Harshith
- **Email**: mmharshith6@gmail.com
- **Phone**: 7411801829
- **GitHub**: https://github.com/mmharshith6-web
- **LinkedIn**: https://www.linkedin.com/in/mmcodes/
- **Portfolio**: https://portfolio2-mu-puce.vercel.app/

## Support
For issues with deployment, check:
1. Vercel documentation: https://vercel.com/docs
2. GitHub repository issues
3. Contact the developer at mmharshith6@gmail.com