# 🎬 MovieBuzz-Predictor

An ML-powered web application that predicts whether a movie is likely to be a **Hit**, **Average**, or **Flop** based on its budget, genre, and other features.

---

## 🚀 Project Overview

**MovieBuzz-Predictor** is a machine learning-based Streamlit app that forecasts the box office success of a movie. It uses a classification model trained on historical movie data (from TMDb), using features such as budget and genre to intelligently predict a film’s performance.

This project showcases:
- Real-world ML deployment using **XGBoost**
- Cleaned and feature-engineered data in **Google Colab**
- A beautiful **Streamlit web app** interface for live predictions
- **GitHub + Streamlit Cloud** integration for sharing your work

---

## 🔍 Problem Statement

Studios often face uncertainty before a movie release. With millions invested, early prediction tools can help producers, marketers, and investors make better decisions. This project aims to predict a movie’s fate — **Hit**, **Average**, or **Flop** — before it hits the screen.

---

## 🧠 Machine Learning Details

- **Model Used:** XGBoost Classifier  
- **Accuracy Achieved:** ~87%  
- **Target Classes:** `['Flop', 'Average', 'Hit']`  
- **Feature Engineering:**  
  - Log-transformed budgets  
  - One-hot encoded genres (Action, Comedy, Drama, Romance, etc.)

---

## 🛠️ Tech Stack

| Layer            | Tools Used                   |
|------------------|------------------------------|
| Data Processing  | Pandas, NumPy                |
| Model Training   | Scikit-learn, XGBoost        |
| App Interface    | Streamlit                    |
| Deployment       | Streamlit Cloud + GitHub     |

---

## 📂 Project Structure

MovieBuzz-Predictor/
├── app.py # Streamlit app source code
├── cine_model.pkl # Trained XGBoost model
├── label_encoder.pkl # Label encoder for class outputs
├── model_training.ipynb # Colab notebook for training & preprocessing
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)# MovieBuzz-Predictor

---

## 🙋‍♀️ About Me

**Rethenya M**  
Electronics & Computer Engineering student passionate about data science, machine learning, and building real-world tech solutions that create impact.  
Currently focused on mastering ML, data engineering, and intelligent systems.

[🔗 LinkedIn](www.linkedin.com/in/rethenya004) • [📧 Email Me](rethenya.m@gmail.com)

---

## 📌 License

This project is open-source and intended for educational and demonstration purposes only.

