🫀 CardioSense AI — Heart Disease Prediction

AI-Powered Heart Health Risk Assessment

CardioSense AI is a machine-learning-based web application designed to demonstrate how cardiovascular health indicators can be processed by a trained classification model to generate a predicted output.

The application features a modern, responsive medical interface built with a teal-and-white color palette, providing a simple and accessible user experience.

«Disclaimer: This project is intended for educational and demonstration purposes only. It is not a medical diagnostic tool and must not be used to make healthcare decisions.»

---

📌 Project Overview

CardioSense AI combines machine learning with web development to demonstrate a complete prediction workflow.

Users can enter the required demographic and cardiovascular feature values through a structured form. The application validates the inputs, applies the saved feature scaler, and passes the processed data to a trained Logistic Regression model.

The resulting prediction is displayed through a dedicated results page.

✨ Key Features

- 🫀 Heart Disease Prediction: Uses a trained machine-learning classification model.
- 🤖 Machine Learning Integration: Integrates Logistic Regression with StandardScaler preprocessing.
- 📝 Interactive Assessment Form: Collects 13 model input features.
- 📊 Prediction Results: Displays the predicted class and the model's estimated probability when available.
- 📋 Input Summary: Shows the values submitted for an assessment.
- 🎨 Modern UI: Features a responsive medical teal-and-white interface.
- 📱 Responsive Design: Supports desktop and mobile screen sizes.
- 🧭 Multi-Page Navigation: Includes Home, Overview, Assessment, Results, and About pages.
- ⚙️ Input Validation: Checks required values and configured input boundaries.
- ☁️ Deployment Preparation: Includes a Vercel entry point and deployment configuration.

🛠️ Technology Stack

Category| Technology
Programming Language| Python
Web Framework| Flask
Machine Learning| Scikit-learn
ML Algorithm| Logistic Regression
Feature Preprocessing| StandardScaler
Data Processing| Pandas, NumPy
Model Serialization| Joblib
Frontend| HTML5, CSS3, JavaScript
Templating Engine| Jinja2
Version Control| Git and GitHub
Deployment Target| Vercel

🧠 Machine Learning Workflow

The application follows these steps:

1. Input Collection: Collects 13 required feature values.
2. Input Validation: Checks the submitted values.
3. Feature Scaling: Applies the previously fitted StandardScaler.
4. Model Inference: Sends the processed features to the saved Logistic Regression model.
5. Result Generation: Obtains the predicted class and, when supported, the model's estimated class probability.
6. Result Presentation: Displays the output and the submitted input summary.

Model Information

- Algorithm: Logistic Regression
- Preprocessing: StandardScaler
- Task: Binary classification
- Input: 13 numerical or dataset-encoded features
- Output: Predicted class

The model and scaler are reused from the existing project rather than being retrained during every prediction.

📂 Project Structure

CardioSense-AI/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│   ├── heart_model.pkl
│   └── scaler.pkl
│
├── dataset/
│   └── heart.csv
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── predict.html
│   ├── result.html
│   ├── about.html
│   └── 404.html
│
├── public/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.svg
│
├── index.py
├── train_model.py
├── requirements.txt
├── vercel.json
├── README.md
└── .gitignore

💻 Installation and Setup

Prerequisites

Make sure you have installed:

- Python 3.10 or a compatible supported version
- pip
- Git
- Visual Studio Code (recommended)

Step 1: Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd CardioSense-AI

Replace "YOUR_GITHUB_REPOSITORY_URL" with your actual repository URL.

Step 2: Create a virtual environment

Windows PowerShell:

python -m venv venv

Activate the environment:

.\venv\Scripts\Activate.ps1

If PowerShell blocks script execution, use Command Prompt instead:

venv\Scripts\activate.bat

Step 3: Install dependencies

python -m pip install -r requirements.txt

Step 4: Verify the required files

Ensure the following files are present:

models/heart_model.pkl
models/scaler.pkl
dataset/heart.csv

The saved model and scaler must match the feature order and preprocessing used by the prediction code.

Step 5: Run the application

From the project root directory, execute:

python -m app.app

Open the application in your browser:

http://127.0.0.1:5000

☁️ Deployment

The project includes a Vercel entry point and configuration for deployment preparation.

To deploy:

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Verify the Python runtime and dependency compatibility.
4. Confirm that the trained model and scaler are available in the deployment.
5. Deploy the application.
6. Test the homepage, static assets, assessment form, and prediction endpoint.

Note: A successful local run does not guarantee a successful Vercel deployment. Deployment must be tested separately.

🔒 Data Privacy and Security

- Avoid collecting unnecessary personal information.
- Do not commit secrets, API keys, or credentials to GitHub.
- Include only trusted model artifacts.
- Review dataset licensing and usage permissions before redistribution.
- Do not use untrusted pickle files because loading them can execute arbitrary code.

⚠️ Limitations

- The output depends on the quality and limitations of the training dataset.
- The model's probability is not necessarily a calibrated clinical risk estimate.
- The application has not been established as a clinically validated diagnostic system.
- A negative prediction does not rule out heart disease.
- A positive prediction does not establish a medical diagnosis.
- Users should consult qualified healthcare professionals for medical concerns.

🎯 Learning Outcomes

This project demonstrates practical experience with:

- Integrating a trained machine-learning model into a Flask application.
- Reusing serialized model and preprocessing artifacts.
- Validating user inputs before inference.
- Building a responsive multi-page web interface.
- Connecting frontend forms with backend prediction logic.
- Organizing a Python project into reusable modules.
- Preparing an application for GitHub version control and cloud deployment.

🙏 Acknowledgment

I would like to express my sincere gratitude to my respected sir for his valuable guidance, encouragement, and support throughout the development of this project.

His guidance has helped me improve my understanding of machine learning integration, application development, and project implementation.

👨‍💻 Author

Yash Kherde

Computer Engineering — Data Science

GitHub: Add your GitHub profile link here.

LinkedIn: Add your LinkedIn profile link here.

---

⭐ If you find this project interesting, consider giving the repository a star.

Disclaimer: CardioSense AI is an educational project and is not intended to diagnose, prevent, or treat any medical condition.
