# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 12:44:42 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st



#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


#creating a function for prediction 

def heartdisease_prediction(input_data):
    

    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)

    #reshape the numpy array as we are predicting for an intance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person does not have a heart disease'
    else:
      return 'The person has heart disease'
  
    
  
def main():
    
    
    st.title('Heart disease prediction web app')
    st.write('*created by Navaneethkrishnan M*')
    st.write("[Buy me a coffee!!☕](https://www.buymeacoffee.com/navaneethnk)")

    
    #getting the data from user
    
    
    age = st.text_input('Age of the patient')
    sex = st.text_input('sex of the patient (1 = male; 0 = female)')
    cp = st.text_input('chest pain type')
    trestbps = st.text_input('resting blood pressure (in mm Hg on admission to the hospital')
    chol = st.text_input('serum cholestoral in mg/dl')
    fbs = st.text_input('(fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)')
    restecg = st.text_input('resting electrocardiographic results')
    thalach = st.text_input('maximum heart rate achieved')
    exang = st.text_input('exercise induced angina (1 = yes; 0 = no)')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    slope = st.text_input('the slope of the peak exercise ST segment')
    ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    thai = st.text_input(' thalassemia 1 = normal; 2 = fixed defect; 3 = reversable defect')
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('heartdisease test result'):
        diagnosis = heartdisease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thai])
        
    st.success(diagnosis)
    
    
    
if __name__== '__main__':
    main()

          
    
    
    
    
    
    
    
    
    
    
