# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:07:51 2020
@author: win10
"""
import json

# pip install fastapi uvicorn pickle

# 1. Library imports
import uvicorn  ##ASGI
from fastapi import FastAPI
from Vocal import Vocal
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import librosa
import requests

# 2. Create the app object
app = FastAPI()
#picke_in = open('mlp_classifier.model', "rb")
#model = pickle.load(picke_in)
with open('mlp_classifier.pkl', 'rb') as pickle_in:
    model = pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}


# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}


@app.post('/predict')
def predict_sentiment(data: Vocal):
    le = LabelEncoder()
    #print(list((data.features.values())))
    predicted_vector = model.predict(list(data.features))
    predicted_proba = predicted_vector[0]
    # for i in range(len(predicted_proba)):
    #     category = le.inverse_transform(np.array([i]))
    #     print(category[0], "\t\t : ", format(predicted_proba[i], '.32f'))
    # for i in range(len(predicted_proba)):
    #     print(predicted_proba[i])
    #     category = le.inverse_transform(np.array([i]))
    #     print(category[0], "\t\t : ", format(predicted_proba[i], '.32f'))

    # for i in range(len(predicted_proba)):
    #     category = le.inverse_transform(np.array([i]))
    #     print(category[0], "\t\t : ", format(predicted_proba[i], '.32f'))
    # create a dictionary mapping each category to its predicted probability
    ## predictions = {le.inverse_transform(np.array([i]))[0]: predicted_proba[i] for i in range(len(predicted_proba))}


    # return predictions

    return {"Predictions": predicted_vector.tolist()}


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    # Load your audio data and compute the MFCC features

    audio_data, sample_rate = librosa.load('../Data-Science/Audio_data/our_audios/wass_calme_1.wav', res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio_data.flatten(), sr=sample_rate, n_mfcc=40)

    # Create a Vocal object with the mfccs data and pass it to the predict_sentiment endpoint
    vocal_data = Vocal(features=mfccs)
    response = requests.post('http://127.0.0.1:8000/predict', json=json.dumps(vocal_data.dict()))
    print(response.json())
# uvicorn main:app --reload

print("oe")