# -*- coding: utf-8 -*-

import numpy as np
import pickle
import os
from collections import Mapping
from flask import Flask, request, render_template

# Load ML model
# model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__,template_folder='templates')

# Bind home function to URL
@app.route('/')
def home():
    return render_template('main.html')

# Bind predict function to URL
# @app.route('/predict', methods =['POST'])
# def predict():
    
#     # Put all form entries values in a list 
#     features = [float(i) for i in request.form.values()]
#     # Convert features to array
#     array_features = [np.array(features)]
#     # Predict features
#     prediction = model.predict(array_features)
    
#     output = prediction
    
#     # Check the output values and retrive the result with html tag based on the value
#     if output == 1:
#         return render_template('main.html', 
#                                result = 'The patient is not likely to have paralysis!')
#     else:
#         return render_template('main.html', 
#                                result = 'The patient is likely to have paralysis!')

if __name__ == '__main__':
#Run the application
  port = os.environ.get("PORT", 5000)
app.run(debug = False,host = "0.0.0.0",port=port )
    
    
