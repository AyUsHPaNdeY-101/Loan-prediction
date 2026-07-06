from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model/loan_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    income = float(request.form['income'])
    loan_amount = float(request.form['loanamount'])
    credit_score = float(request.form['creditscore'])

    prediction = model.predict([[age, income, loan_amount, credit_score]])

    return render_template('index.html', prediction_text=f'Loan Approved Status: {"Approved" if prediction[0] == 1 else "Not Approved"}')

if __name__ == "__main__":
    app.run(debug=True)