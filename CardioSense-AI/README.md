
# CardioSense AI

CardioSense AI is an educational heart-health risk assessment
web application built with Flask and scikit-learn.

## Features

- Responsive medical teal-and-white interface
- 13-feature input form
- Existing Logistic Regression model integration
- StandardScaler preprocessing
- Model result and input summary
- Flask routes and Vercel deployment entry point

## Technology

- Python
- Flask
- NumPy and pandas
- scikit-learn
- Joblib
- HTML, CSS and JavaScript

## Project setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy the existing trained model and scaler to:

- `models/heart_model.pkl`
- `models/scaler.pkl`

Place the training dataset at:

- `dataset/heart.csv`

## Run locally

From the project root:

```powershell
python -m app.app
```

Open http://127.0.0.1:5000

## Retrain the model

Only when necessary:

```powershell
python train_model.py
```

The dataset must contain the 13 expected feature columns and
a binary `target` column.

## Deployment

Push the project to GitHub and import the repository into Vercel.
Verify that the Python runtime supports all installed dependencies
and that the model artifacts are included in the deployment.

## Disclaimer

This project is for educational and demonstration purposes only.
It is not a medical device and must not be used to diagnose,
exclude or treat heart disease.
