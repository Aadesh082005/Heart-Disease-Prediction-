# Heart Disease Prediction App

An educational machine learning application built with
Python, Scikit-learn, and Streamlit.

## Features

- Heart disease dataset exploration
- Data preprocessing
- Random Forest classification
- Model evaluation
- Interactive prediction form
- Dataset visualization
- Automated tests

## Requirements

- Python 3.10 or a compatible supported version
- pip
- VS Code (recommended)

## Installation

Create a virtual environment:

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

## Dataset

Place a compatible CSV dataset at:

    data/raw/heart.csv

The expected target column is `target`.

The expected features are:

- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

Verify column definitions and label encoding against
the dataset's documentation before training.

## Train the Model

    python -m src.models.train_model

## Evaluate the Model

    python -m src.models.evaluate_model

## Run the Application

    streamlit run app.py

## Run Tests

    python -m pytest tests -v

## Medical Disclaimer

This project is for educational purposes only. It is not a
medical diagnostic tool and must not be used to diagnose,
rule out, or treat heart disease.