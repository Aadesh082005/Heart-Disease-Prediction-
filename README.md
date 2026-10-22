# ❤️ CardioAI — Heart Disease Prediction App

An interactive Machine Learning web application built with Python and Streamlit to explore heart disease datasets, generate model predictions, and visualize model performance.

## 🚀 Overview

CardioAI demonstrates how machine learning can be applied to structured health-related data through an interactive dashboard. Users can enter dataset-compatible features, view model outputs, explore data visualizations, and review classification metrics.

**Note:** This is an educational project, not a clinically validated medical tool. Predictions must not be used for diagnosis or treatment decisions.

## ✨ Features

- **Interactive Dashboard:** Clean, modern interface with a dark theme.
- **Heart Disease Prediction:** Enter feature values and view the trained model's output.
- **Health Insights:** Explore dataset distributions and feature correlations.
- **Model Performance:** Review accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrix when available.
- **Data Preprocessing:** Validate dataset columns and prepare data for machine learning.
- **Machine Learning Pipeline:** Train and evaluate a Random Forest classifier.
- **Modular Architecture:** Separate modules for data processing, feature engineering, training, prediction, and visualization.
- **Automated Tests:** Basic tests for preprocessing, prediction, and model behavior.

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Plotly, Matplotlib
- **Model Persistence:** Joblib
- **Testing:** Pytest
- **Development Environment:** Visual Studio Code

## 📂 Project Structure

```text
Heart-Disease-Prediction/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── assets/
│   └── styles/
│       └── custom.css
├── data/
│   ├── raw/
│   │   └── heart.csv
│   └── processed/
├── models/
│   └── model_metadata.json
├── notebooks/
│   └── heart_disease_eda.ipynb
├── pages/
│   ├── 1_Heart_Prediction.py
│   ├── 2_Health_Insights.py
│   ├── 3_Model_Performance.py
│   └── 4_About_Project.py
├── reports/
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── utils/
│   └── visualization/
└── tests/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Add the dataset

Place your compatible CSV dataset at:

```text
data/raw/heart.csv
```

The dataset should contain the 13 expected input features and a target column named `target`. Check the project's configuration and preprocessing code for the exact column names and label requirements.

### 5. Train the machine learning model

Run the training script from the project root:

```bash
python -m src.models.train_model
```

This should generate the trained model and evaluation files at the paths configured by the project.

### 6. Run the application

```bash
streamlit run app.py
```

Streamlit will display a local URL, usually `http://localhost:8501`. Open it in your browser.

## 📊 Model Evaluation

The application can display metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC, when available
- Confusion matrix

Actual results depend on the dataset, preprocessing, train/test split, and model configuration. No performance figures are claimed in advance.

## 🧪 Run Tests

From the project root, run:

```bash
python -m pytest -v
```

## 🔮 Future Enhancements

- Improve data validation and error handling.
- Add reproducible model experiments and cross-validation.
- Add model explainability using SHAP or similar tools.
- Improve accessibility and responsive design.
- Evaluate performance on independent datasets.
- Add deployment and continuous integration workflows.

## 🎓 Learning Outcomes

This project demonstrates practical skills in Python development, data preprocessing, machine learning, model evaluation, data visualization, modular project design, and interactive web application development.

## ⚠️ Disclaimer

CardioAI is intended for educational and demonstration purposes only. It has not been established as a clinically validated diagnostic system. Model outputs may be inaccurate and must not be used to diagnose or rule out heart disease, select treatment, or delay professional medical care.

## 👨‍💻 Author

**YOUR NAME**

GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

## 📄 License

This project is available under the MIT License if you choose to distribute it under those terms. Add a `LICENSE` file before claiming that the repository is MIT-licensed.
