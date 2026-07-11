# 🏦 Loan Predictor: Machine Learning Web App

## 📝 Overview
This project is an end-to-end Machine Learning web application that predicts whether a user's loan will be approved or denied based on their financial profile. It demonstrates a complete data pipeline: from training a classification algorithm using Python and pandas to deploying it as an interactive web interface using Flask.

## ✨ Key Features
*   **Predictive Algorithm:** Implements a Decision Tree Classifier (`max_depth=4`) using `scikit-learn` to evaluate features such as age, income, loan amount, and credit score.
*   **Model Serialization:** Utilizes `joblib` to export the trained model (`loan_model.pkl`), allowing the web application to make instant predictions without retraining.
*   **Interactive Web Interface:** Features a Flask-powered frontend with an HTML form that accepts user input and dynamically renders the "Approved" or "Not Approved" status.
*   **Structured Data Handling:** Implements proper directory management for datasets (`data/`) and serialized models (`model/`).

## 💻 Tech Stack & Dependencies
*   **Backend Framework:** Flask
*   **Machine Learning:** Scikit-Learn (DecisionTreeClassifier)
*   **Data Processing:** Pandas
*   **Model Serialization:** Joblib

## 📂 Project Structure
*   `app.py`: The main Flask application script that handles routing and prediction logic.
*   `train_model.py`: The data processing and machine learning script used to train the classifier.
*   `data/loan_data.csv`: The dataset containing historical financial profiles and approval statuses used to train the model.
*   `model/loan_model.pkl`: The serialized Decision Tree model.
*   `templates/index.html`: The HTML form template used by Flask for the frontend interface.

## 🚀 How to Run Locally

### 1. Clone the Repository and Install Dependencies
Ensure you have Python installed, then clone this project and install the necessary libraries using your terminal:

```bash
git clone [https://github.com/AyUsHPaNdeY-101/YOUR_REPO_NAME.git](https://github.com/AyUsHPaNdeY-101/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
pip install pandas scikit-learn flask joblib
```

### 2. Set Up Directories & Train the Model
Make sure you have created the `data/` and `model/` folders and placed `loan_data.csv` inside the `data/` folder. Then, generate the prediction model by running the training script:

```bash
python train_model.py
```
*Note: This will output the model's accuracy in your terminal and save `loan_model.pkl` in the `model/` directory.*

### 3. Start the Flask Server
Launch the web application by running the main Flask script:

```bash
python app.py
```

### 4. View the Application
Once the server is running, open your web browser and navigate to:
http://127.0.0.1:5000/

Enter values for Age, Income, Credit Score, and Loan Amount in the form, then submit it to see the machine learning model's approval prediction in real-time!

---
