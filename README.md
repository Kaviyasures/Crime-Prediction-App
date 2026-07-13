<h1 align="center">🔍 Crime Prediction Using Machine Learning</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Flask-red.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Library-Scikit--Learn-orange.svg" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Status-Completed-success.svg" alt="Status">
</p>

## 📝 Project Abstract
The objective of this project is to tackle a vital issue in society by analyzing and predicting crime occurrences[cite: 1]. Identifying crime patterns allows for the deployment of unique approaches in specific crime category regions to improve security measures[cite: 1]. This system predicts regions that have a high probability for crime occurrences and visualizes crime-prone areas using machine learning and data mining techniques[cite: 1].

## 👥 Contributors
This project was developed as a Bachelor of Computer Applications (BCA) mini-project for the 2023-2024 academic year[cite: 2].
* **Nivetha L.** (212104972)[cite: 2]
* **Kaviya S.** (212104961)[cite: 2]
* **Roshni S.** (212104979)[cite: 2]
* **Institution:** St. Anne's Arts and Science College (University of Madras)[cite: 2]
* **Under the guidance of:** Smt. D.S. Eunice Little Dani[cite: 2]

## 🏗️ System Architecture & Workflow
The system pipeline follows a structured data science workflow[cite: 1]:
1. **Data Collection:** Importing the historical crime dataset[cite: 1].
2. **Data Preprocessing:** Cleaning data, handling missing values, and formatting[cite: 1].
3. **Feature Extraction:** Extracting temporal and geospatial attributes[cite: 1].
4. **Model Training & Classification:** Splitting data into training and testing sets to evaluate algorithms[cite: 1].
5. **Prediction Output:** Displaying the finalized predicted crime hotspot via the web application[cite: 1].

## 🧠 Machine Learning Algorithms Evaluated
The proposed system calibrated and evaluated multiple classification algorithms to determine the most effective model for this dataset[cite: 1]:
* **K-Nearest Neighbors (KNN)**[cite: 1]
* **Decision Tree Classifier**[cite: 1]
* **Random Forest Classifier** (Selected for deployment due to high accuracy)[cite: 1]

## 📊 Dataset & Features
The predictive model analyzes specific spatiotemporal inputs to output a predicted crime category[cite: 1].

**Input Features:**
* Temporal Data: `month`, `day`, `hour`, `dayofyear`, `weekofyear`[cite: 1].
* Geospatial Data: `latitude`, `longitude`[cite: 1].

**Target Classifications:**
* **Act 379:** Robbery[cite: 1]
* **Act 13:** Gambling[cite: 1]
* **Act 279:** Accident[cite: 1]
* **Act 323:** Violence[cite: 1]
* **Act 363:** Kidnapping[cite: 1]
* **Act 302:** Murder[cite: 1]

## 💻 Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/Kaviyasures/Crime-Prediction-App.git](https://github.com/Kaviyasures/Crime-Prediction-App.git)
cd Crime-Prediction-App
