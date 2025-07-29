import gradio as gr
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction function
def predict_score(hours):
    try:
        hours = float(hours)
        score = model.predict(np.array([[hours]]))[0]
        return f"📘 Predicted Score: {score:.2f}"
    except ValueError:
        return "❌ Please enter a valid number."

# Gradio Interface
interface = gr.Interface(
    fn=predict_score,
    inputs=gr.Number(label="Enter Study Hours"),
    outputs=gr.Textbox(label="Prediction"),
    title="📊 Student Score Predictor",
    description="Enter the number of hours a student studies to predict their score using a linear regression model.",
    theme="default"
)

# Launch app
if __name__ == "__main__":
    interface.launch(share=True)
