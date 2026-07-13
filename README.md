📝 Project Abstract

The objective of this project is to tackle a vital issue in society by analyzing and predicting crime occurrences. Identifying crime patterns allows for the deployment of unique approaches in specific crime category regions to improve security measures. This system predicts regions that have a high probability for crime occurrences and visualizes crime-prone areas using machine learning and data mining techniques.

👥 Contributors

This project was developed as a Bachelor of Computer Applications (BCA) mini-project for the 2023-2024 academic year.

Nivetha L. (212104972)

Kaviya S. (212104961)

Roshni S. (212104979)

Institution: St. Anne's Arts and Science College (University of Madras)

Under the guidance of: Smt. D.S. Eunice Little Dani

🏗️ System Architecture & Workflow

The system pipeline follows a structured data science workflow:

Data Collection: Importing the historical crime dataset.

Data Preprocessing: Cleaning data, handling missing values, and formatting.

Feature Extraction: Extracting temporal and geospatial attributes.

Model Training & Classification: Splitting data into training and testing sets to evaluate algorithms.

Prediction Output: Displaying the finalized predicted crime hotspot via the web application.

🧠 Machine Learning Algorithms Evaluated

The proposed system calibrated and evaluated multiple classification algorithms to determine the most effective model for this dataset:

K-Nearest Neighbors (KNN)

Decision Tree Classifier

Random Forest Classifier (Selected for deployment due to high accuracy)

📊 Dataset & Features

The predictive model analyzes specific spatiotemporal inputs to output a predicted crime category.

Input Features:

Temporal Data: month, day, hour, dayofyear, weekofyear.

Geospatial Data: latitude, longitude.

Target Classifications:

Act 379: Robbery

Act 13: Gambling

Act 279: Accident

Act 323: Violence

Act 363: Kidnapping

Act 302: Murder

💻 Local Setup & Installation

1. Clone the repository

git clone https://github.com/Kaviyasures/Crime-Prediction-App.git
cd Crime-Prediction-App


2. Install required dependencies

pip install -r requirements.txt


3. Run the Flask application

python app.py


Navigate to http://127.0.0.1:5000 in your web browser to access the interface.
