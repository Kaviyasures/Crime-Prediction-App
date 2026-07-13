import os
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from twilio.rest import Client
from dotenv import load_dotenv
import pickle

# Load secure environment variables
load_dotenv()

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

# Secure Twilio credentials pulled from a hidden .env file
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
target_phone_number = os.getenv('TARGET_PHONE_NUMBER')

client = Client(account_sid, auth_token)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI and sending Twilio message
    '''
    float_features = [float(x) for x in request.form.values()]
    test_vector = np.reshape(np.asarray(float_features), (1, 7))
    p = np.array(model.predict(test_vector)[0])

    labels = ['Robbery', 'Gambling', 'Accident', 'Violence', 'Kidnapping', 'Murder']
    predictions = [labels[i] for i in range(len(p)) if p[i] == 1]

    if not predictions:
        output = 'No specific crime predicted'
    else:
        output = ', '.join(predictions)

    # Sending Twilio message securely
    message_body = f'Crime Prediction: {output}'
    
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=target_phone_number
        )
        print(f"Message sent to {target_phone_number} SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

    return render_template('index.html', prediction_text='Crime: {}'.format(output))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)