import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import statsmodels.api as sm
import numpy as np


app = Flask(__name__)

def load_models():
    file_name = "models/test_file_final_stats3.pickle"
    model = sm.load(file_name)
    return model

@app.route('/', methods=['GET', 'POST'])
def home():
    return "hello world"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # parse input features from request
    request_json = request.get_json()
    data_list = []

    # labelencoder = LabelEncoder()

#for farm size
    farm_size = request_json['farm_size']
    farm_size = np.log10(farm_size)
    data_list.append(farm_size)
#for temperature
    temperature = request_json['temperature']
    data_list.append(temperature)

#for rainfall
    rainfall = request_json['rainfall']
    data_list.append(rainfall)


#changing the string values in the list to float values
    x = [float(v) for v in data_list]
    print(x)

     # load model and predict
    model = load_models()
    prediction = model.predict(x)[0]
    # prediction = 19.098765
    prediction = round(prediction, 1)
    prediction = 10**prediction
    prediction = round(prediction, 1)
    response = json.dumps({'response': prediction})

    return response, 200


if __name__ == '__main__':
    application.run(debug=True)




