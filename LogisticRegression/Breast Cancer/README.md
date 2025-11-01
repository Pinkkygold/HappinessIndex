

# ❤️ Simple Heart Attack Predictor

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5.0-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://machine-learning-projects-s5t4.onrender.com)

A minimal yet functional **machine learning web app** that predicts the **risk of heart attack** based on a single input feature — **age**.
The model uses **Logistic Regression** and is deployed with **Flask** on Render.

🔗 **Live Demo:** [https://machine-learning-projects-s5t4.onrender.com](https://machine-learning-projects-s5t4.onrender.com)

---

## 🧠 Overview

This project demonstrates how to:

* Train a simple **Logistic Regression model** in Python
* Serialize the trained model using `pickle`
* Build an **interactive Flask web app**
* Deploy it on **Render Cloud**

Despite being based on one feature (`Age`), it provides a great example of **end-to-end ML deployment** — from model creation to public hosting.

---

## 🧩 Tech Stack

| Component        | Description                                |
| ---------------- | ------------------------------------------ |
| **Python**       | Core programming language                  |
| **Flask**        | Lightweight backend web framework          |
| **Scikit-Learn** | For building the logistic regression model |
| **NumPy**        | Numerical computation and data handling    |
| **HTML/CSS**     | Frontend interface for user interaction    |
| **Render**       | Cloud deployment platform                  |

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Pinkkygold/simple-heartattack-predictor.git
   cd simple-heartattack-predictor
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # (Mac/Linux)
   .venv\Scripts\activate      # (Windows)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run locally**

   ```bash
   python app.py
   ```

   or using **Gunicorn** for production-style run:

   ```bash
   gunicorn app:app --bind 0.0.0.0:5000
   ```

5. **Open in browser**

   ```
   http://127.0.0.1:5000
   ```

---

## 🖥️ Project Structure

```
simple-heartattack-predictor/
│
├── app.py                     # Flask app
├── Heartattack.pkl            # Trained logistic regression model
├── requirements.txt           # Dependencies
├── static/
│   └── style.css              # Styling for frontend
├── templates/
│   └── index.html             # HTML interface
└── Procfile                   # For Render/Heroku deployment
```

---

## 🌍 Deployment (on Render)

1. Push this repository to GitHub
2. Connect it to **Render**
3. Add a **web service**
4. Use this start command:

   ```
   gunicorn app:app
   ```
5. That’s it! Render will automatically build and host your app.

---

## 📊 Model Details

* **Algorithm:** Logistic Regression
* **Input Feature:** Age
* **Output:** Binary prediction

  * `1` → High risk of heart attack
  * `0` → Low risk

> The probability output provides an interpretable measure of confidence.

---

## 🧑‍💻 Author

**Awab Elkhair**
📍 Machine Learning Engineer | Researcher | Volunteer
🌐 [ResearchGate](https://www.researchgate.net/profile/Awab-Abdalla)
💼 [GitHub: Pinkkygold](https://github.com/Pinkkygold)

---

## 🪶 License

This project is licensed under the **MIT License** — feel free to fork and use it for your learning or portfolio.

---

Would you like me to include a **preview image (screenshot)** section and a **requirements.txt** content block (with exact versions for Flask, scikit-learn, etc.) so it’s deployment-ready?

