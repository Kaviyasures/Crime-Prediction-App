# 🚨 Crime Prediction Machine Learning App

An end-to-end machine learning web application that predicts the likelihood of specific crime types based on temporal and geospatial data, featuring real-time SMS alerts.

## 📖 Project Overview
Predicting crime hotspots and incident types is a crucial task for modern law enforcement and city planning. This project utilizes historical crime data to train machine learning models to classify potential incidents. By analyzing temporal features (month, day, time) and geospatial features (latitude, longitude), the model predicts the occurrence of six distinct categories: **Robbery, Gambling, Accident, Violence, Kidnapping, and Murder**.

## ✨ Key Features
* **Machine Learning Pipeline:** Includes comprehensive data preprocessing, feature engineering, and model evaluation.
* **Algorithm Comparison:** Evaluated K-Nearest Neighbors (KNN), Decision Trees, and Random Forest classifiers.
* **Interactive Web Interface:** A lightweight, user-friendly HTML/CSS frontend powered by Flask.
* **Real-Time SMS Alerts:** Integrated with the **Twilio API** to instantly notify users of the predicted crime via automated text messages.

## 🛠️ Technology Stack
* **Backend:** Python, Flask
* **Data Science & ML:** Scikit-Learn, Pandas, NumPy, Jupyter Notebook
* **Frontend:** HTML, CSS
* **APIs:** Twilio Cloud Communications

## 🚀 Local Installation & Setup

To run this project locally on your machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/Kaviyasures/Crime-Prediction-App.git](https://github.com/Kaviyasures/Crime-Prediction-App.git)
cd Crime-Prediction-App
