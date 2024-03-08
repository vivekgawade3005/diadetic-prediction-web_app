# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
print("2626")
import numpy as np
import pickle
import streamlit as st
print("122")
 #loating the saved model 
a = pickle.load(open("F:/drdo/trained_model (1).sav","rb"))
print("2518")

input_data=(6,148,72,35,0,33.6,0.627,50)
#  changing the input_data to numpy array
input_data_as_numpy_array=np.asarray(input_data)
#  reshape
input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
#  standardiz the the data
# std_data=scaler.transform(input_data_reshape)
# print(std_data)
prediction=a.predict(input_data_reshape)
print(prediction)
if (prediction[0] == 0):
  print("the person is not diabetic")
else:
  print(" the person is diabetic")
  
  
  def main():
       # giving title 
       st.title("Diabetes orediction web app")
        
       #geting the input data from uses
        pregna