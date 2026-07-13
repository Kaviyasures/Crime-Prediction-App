🚨 Crime Prediction Using Machine Learning

A predictive analytics web application developed to forecast spatial-temporal crime hotspots. Originally developed as an academic project for St. Anne's Arts and Science College.

📖 Project Abstract

The objective of this project is to tackle a vital issue in society: Crime. By analyzing historical crime data trends, this system identifies crime patterns and correlates spatial and temporal factors to predict regions with a high probability of crime occurrences. This proactive approach allows law enforcement to deploy unique strategies in specific regions, ultimately aiding in the mitigation of crime rates.

🎯 Problem Statement & Proposed System

Traditional crime prediction methods often overlook complex socio-economic and temporal factors, leading to limited accuracy (e.g., traditional SVM models).

Our Proposed System:
This project employs advanced ensemble machine learning algorithms (Random Forest, XGBoost, and AdaBoost) alongside standard models (KNN, Decision Trees). By extracting detailed temporal features from timestamps and mapping them against geographical coordinates, the system achieves higher predictive accuracy and faster performance.

✨ Key Features

Temporal Feature Extraction: Automatically breaks down timestamps into specific features: Month, Day, Hour, Day of the Year, and Week of the Year.

Geospatial Mapping: Utilizes Latitude and Longitude to pinpoint crime hotspots.

Multi-Class Classification: Predicts the likelihood of 6 specific incident types:

Robbery (Act 379)

Gambling (Act 13)

Accident (Act 279)

Violence (Act 323)

Kidnapping (Act 363)

Murder (Act 302)

Interactive Web Interface: A lightweight GUI where users can input the 7 temporal/spatial features and receive an instant crime prediction.

🛠️ Technology Stack

Programming Language: Python 3

Data Science & ML: Pandas, NumPy, Scikit-Learn (RandomForestClassifier, KNeighborsClassifier, DecisionTreeClassifier)

Data Visualization: Matplotlib, Seaborn

Backend: Flask

Development Environment: Jupyter Notebook / Anaconda Navigator

🚀 Local Installation & Setup

To run this project locally on your machine, follow these steps:

1. Clone the repository:

git clone https://github.com/Kaviyasures/Crime-Prediction-App.git
cd Crime-Prediction-App


2. Install dependencies:

pip install -r requirements.txt


3. Run the Application:

python app.py


The application will be hosted locally. Open your web browser and navigate to http://127.0.0.1:5000.

💡 How to Use the App

Launch the application.

Enter the temporal data into the fields: month, day, hour, dayofyear, and weekofyear.

Input the geospatial coordinates: latitude and longitude.

Click Predict the Crime. The system will process the input vector through the saved model.pkl (Random Forest) and output the most probable crime category on the screen.

👥 Project Authors

Kaviya. S
Nivetha. L
Roshni. S(Guided by Smt. D.S. Eunice Little Dani - Department of Computer Applications)
