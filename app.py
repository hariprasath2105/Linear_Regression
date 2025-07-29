from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        try:
            hours = float(request.form["hours"])
            score = model.predict(np.array([[hours]]))[0]
            prediction = f"Predicted Score: {score:.2f}"
        except ValueError:
            prediction = "Invalid input. Please enter a number."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
