<h1 align="center">🔍 Crime Prediction Using Machine Learning</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Flask-red.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Library-Scikit--Learn-orange.svg" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Status-Completed-success.svg" alt="Status">
</p>

## 📝 Project Abstract
The objective of this project is to address a vital societal issue by analyzing and predicting crime occurrences. Identifying crime patterns allows for the deployment of targeted approaches in specific regions to improve security measures. This system forecasts areas that have a high probability for incidents and visualizes crime-prone locations utilizing data mining techniques.

## 👥 Contributors
This project was developed as a Bachelor of Computer Applications (BCA) mini-project for the 2023-2024 academic year.
* **Nivetha L.** (212104972)
* **Kaviya S.** (212104961)
* **Roshni S.** (212104979)
* **Institution:** St. Anne's Arts and Science College (University of Madras)
* **Under the guidance of:** Smt. D.S. Eunice Little Dani

## 🏗️ System Architecture & Workflow
The system pipeline follows a structured data science workflow:
* **Data Collection:** Importing the historical crime dataset.
* **Data Preprocessing:** Cleaning data, handling missing values, and formatting.
* **Feature Extraction:** Extracting temporal and geospatial attributes.
* **Model Training & Classification:** Splitting data into training and testing sets to evaluate algorithms.
* **Prediction Output:** Displaying the finalized predicted crime hotspot via the web application.

## 🧠 Machine Learning Algorithms Evaluated
The proposed system calibrated and evaluated multiple classification algorithms to determine the most effective model:
* **K-Nearest Neighbors (KNN)**
* **Decision Tree Classifier**
* **Random Forest Classifier** (Selected for deployment due to high accuracy)

## 📊 Dataset & Features
The predictive model analyzes specific spatiotemporal inputs to output a predicted crime category.

**Input Features:**
* **Temporal Data:** `month`, `day`, `hour`, `dayofyear`, `weekofyear`
* **Geospatial Data:** `latitude`, `longitude`

**Target Classifications:**
* **Act 379:** Robbery
* **Act 13:** Gambling
* **Act 279:** Accident
* **Act 323:** Violence
* **Act 363:** Kidnapping
* **Act 302:** Murder

## 💻 Local Setup & Installation

**1. Clone the repository**

    git clone https://github.com/Kaviyasures/Crime-Prediction-App.git
    cd Crime-Prediction-App

**2. Install required dependencies**

    pip install -r requirements.txt

**3. Run the Flask application**

    python app.py

*Navigate to `http://127.0.0.1:5000` in your web browser to access the interface.*

---
<p align="center"><i>"Towards Fullness Through Excellence and Relevance"</i></p>
