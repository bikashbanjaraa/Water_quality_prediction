import streamlit as st
import pickle

with open('model.pickle','rb') as file:
    model = pickle.load(file)

st.title('Water Quality Prediction')


ph = st.text_input("enter ph")
Hardness = st.text_input("enter Hardness ")
Solids = st.text_input("enter Solids")
Chloramines = st.text_input("enter Chloramines")
Sulfate = st.text_input("enter Sulfate")
Conductivity = st.text_input("enter Conductivity")
Organic_carbon = st.text_input("enter organic_carbon")
Trihalomethanes= st.text_input("enter Trihalomethanes")
Turbidity = st.text_input("enter Turbidity")


if st.button("predict water quality"):
    y_pred = model.predict([[ph,Hardness,Solids,Chloramines,Sulfate,
                             Conductivity,
                             Organic_carbon,Trihalomethanes,Turbidity]])
    
    st.write(y_pred)