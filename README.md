
# 🎯 Student Score Predictor

A simple web application built with Python and Gradio that predicts a student's exam score based on the number of hours studied, using a **Linear Regression model**.

---

## 🧠 Overview

This project demonstrates how to use Linear Regression for predicting numerical outcomes. It takes input as **hours studied** and predicts the **score** using a pre-trained model (`model.pkl`) trained on a dataset of student scores.

---

## 📂 Project Structure

```
student-score-predictor/
│
├── model.py               # Script for training and saving the Linear Regression model
├── model.pkl              # Trained and serialized model
├── student_scores.csv     # Dataset used for training
├── requirements.txt       # Dependencies for the project
├── .gradio/               # Gradio app and config
└── README.md              # Project documentation
```

---

## 🧪 Dataset

**File**: `student_scores.csv`

**Features**:
- `Hours`: Number of hours studied
- `Scores`: Marks obtained

---

## 🚀 Features

- Input number of study hours and get predicted exam scores.
- Built using Python, scikit-learn, and Gradio.
- Trained using simple Linear Regression.
- Lightweight and easy to deploy.

---

## 🛠 Tech Stack

| Technology     | Use                  |
|----------------|----------------------|
| Python         | Core language        |
| scikit-learn   | Machine Learning     |
| Pandas         | Data manipulation    |
| NumPy          | Numeric operations   |
| Gradio         | Web-based UI         |

---

## 🛠 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/hariprasath2105/Linear-Regression.git
cd Linear-Regression
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Train the Model (if needed)
```bash
python model.py
```

---

## 💡 Usage

Once everything is set up, run the Gradio interface:

```bash
python model.py
```

---

## 📸 Screenshots

### 📥 Input UI
<img width="1364" height="339" alt="image" src="https://github.com/user-attachments/assets/17dfea1f-1df2-4320-b169-a791aa14f96b" />


### 📈 Output Prediction
<img width="1366" height="310" alt="image" src="https://github.com/user-attachments/assets/bee5ca9d-d8fd-4c97-9f93-121a565b8c5d" />

---

## 🙋‍♂️ Author

**Hari Prasath S**  
[GitHub Profile](https://github.com/hariprasath2105)

---
