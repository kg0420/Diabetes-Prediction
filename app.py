from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
model = joblib.load("Diabetese_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            Glucose = float(request.form.get("Glucose"))
            BloodPressure = float(request.form.get("BloodPressure"))
            Insulin = float(request.form.get("Insulin"))
            BMI = float(request.form.get("BMI"))
            DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
            Age = float(request.form.get("Age"))

            # Create input dataframe (exclude Outcome column since model predicts it)
            inputs = pd.DataFrame([[Glucose, BloodPressure, Insulin, BMI, 
                                    DiabetesPedigreeFunction, Age]],
                                  columns=['Glucose', 'BloodPressure', 'Insulin', 
                                           'BMI', 'DiabetesPedigreeFunction', 'Age'])
            
            prediction = model.predict(inputs)[0]
            if prediction == 1:
                result = "Diabetic"
            else:
                result = "Non Diabetic"
            
            return render_template("index.html", message=f"Result: {result}")

        except Exception as e:
            return render_template("index.html", message=f"ERROR: {e}")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
