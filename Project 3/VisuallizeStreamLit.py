import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image
from keras.models import load_model

#@app.route('/')
def welcome():
    return "Welcome All"

model=load_model("modelpredictBDS.h5")
def predict_note_authentication(Type,Acreage,Direction,BathRoom,FrontHouse,LivingRoom,BedRoom,Juridical):
    test_data=np.array([Type,Acreage,Direction,BathRoom,FrontHouse,LivingRoom,BedRoom,Juridical])
    prediction=model.predict(test_data.reshape(1,8),batch_size=1)
    return prediction



def main():
    st.title("Dự đoán giá bất động sản Hà Nội")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit House Predict App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Type = st.number_input("Type")
    Acreage = st.number_input("Acreage")
    Direction = st.number_input("Direction")
    BathRoom = st.number_input("BathRoom")
    FrontHouse = st.number_input("FrontHouse",)
    LivingRoom = st.number_input("LivingRoom",)
    BedRoom = st.number_input("BedRoom")
    Juridical = st.number_input("Juridical")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Type,Acreage,Direction,BathRoom,FrontHouse,LivingRoom,BedRoom,Juridical)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
    
    
    