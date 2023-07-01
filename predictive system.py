# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('D:/deploy ml/trained_model.sav', 'rb'))

#building a predictive system
input_data = (58,1,0,114,318,0,2,140,0,4.4,0,3,1)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for an intance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print('The person does not have a heart disease')
else:
  print('The person has heart disease')