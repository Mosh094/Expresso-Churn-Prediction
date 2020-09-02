# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 02:10:20 2020

@author: HP EliteBook 840
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in=open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)

def welcome():
    return "welcome All"

def Expresso_Churn_Prediction(REGION,TENURE,MONTANT,FREQUENCE_RECH,REVENUE,ARPU_SEGMENT,FREQUENCE,DATA_VOLUME,ON_NET,ORANGE,TIGO,ZONE1,ZONE2,REGULARITY,TOP_PACK,FREQ_TOP_PACK):


    """Let's Predict Expresso Churn 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: REGION
        in: query
        type: number
        required: true
      - name: TENURE
        in: query
        type: number
        required: true
      - name: MONTANT
        in: query
        type: number
        required: true
      - name: FREQUENCE_RECH
        in: query
        type: number
        required: true
      - name: REVENUE
        in: query
        type: number
        required: true
      - name: ARPU_SEGMENT
        in: query
        type: number
        required: true
      - name: FREQUENCE
        in: query
        type: number
        required: true
      - name: DATA_VOLUME
        in: query
        type: number
        required: true
      - name: ON_NET
        in: query
        type: number
        required: true
      - name: ORANGE
        in: query
        type: number
        required: true
      - name: TIGO
        in: query
        type: number
        required: true
      - name: ZONE1
        in: query
        type: number
        required: true
      - name: ZONE2
        in: query
        type: number
        required: true
      - name: REGULARITY
        in: query
        type: number
        required: true
      - name: TOP_PACK
        in: query
        type: number
        required: true
      - name: FREQ_TOP_PACK
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """

    prediction=classifier.predict([[REGION,TENURE,MONTANT,FREQUENCE_RECH,REVENUE,ARPU_SEGMENT,FREQUENCE,DATA_VOLUME,ON_NET,ORANGE,TIGO,ZONE1,ZONE2,REGULARITY,TOP_PACK,FREQ_TOP_PACK]])
    print(prediction)
    return "The predicted value is"+ str(prediction)

def main():
    st.title("Malicious URL Prediction App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Customer Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    REGION=st.text_input("REGION","Type Here")
    TENURE=st.text_input("TENURE","Type Here")
    MONTANT=st.text_input("MONTANT","Type Here")
    FREQUENCE_RECH=st.text_input("FREQUENCE_RECH","Type Here")
    REVENUE=st.text_input("REVENUE","Type Here")
    ARPU_SEGMENT=st.text_input("ARPU_SEGMENT","Type Here")
    FREQUENCE=st.text_input("FREQUENCE","Type Here")
    DATA_VOLUME=st.text_input("DATA_VOLUME","Type Here")
    ON_NET=st.text_input("ON_NET","Type Here")
    ORANGE=st.text_input("ORANGE","Type Here")
    TIGO=st.text_input("TIGO","Type Here")
    ZONE1=st.text_input("ZONE1","Type Here")
    ZONE2=st.text_input("ZONE2","Type Here")
    REGULARITY=st.text_input("REGULARITY","Type Here")
    TOP_PACK=st.text_input("TOP_PACK","Type Here")
    FREQ_TOP_PACK=st.text_input("FREQ_TOP_PACK","Type Here")
    result=""
    if st.button("Predict"):
        result=Expresso_Churn_Prediction(REGION,TENURE,MONTANT,FREQUENCE_RECH,REVENUE,ARPU_SEGMENT,FREQUENCE,DATA_VOLUME,ON_NET,ORANGE,TIGO,ZONE1,ZONE2,REGULARITY,TOP_PACK,FREQ_TOP_PACK)
    st.success('The Customer Churn Prediction is {}'.format(result))
    if st.button("Prediction Note"):
        st.text("0=customer stayed, 1=customer churned")

if __name__=='__main__':
    main()