#CNG ->0,Petrol->2,Diesel->1
#Automatic -> 0,Manual->1
#Order of the X-> 'Year', 'Kms_Driven', 'Fuel_Type', 'Transmission', 'Owner'


import streamlit as st
import joblib
import numpy as np

scaler=joblib.load("scaler.pkl")
model=joblib.load("model.pkl")


st.title("Used Car Price Prediction")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

year=st.number_input("Enter the year" ,min_value=2000,max_value=2025,value=2014)

km_driven=st.number_input("Enter km driven",min_value=1000,max_value=500000,value=50000)

fuel_type=st.selectbox('Enter fuel type',["CNG","Diesel","Petrol"])

transmission=st.selectbox("Enter the transmission type",["Automatic","Manual"])

owner=st.number_input("Enter the number of owners",min_value=0,max_value=3,value=1)


st.divider()

predictbutton=st.button("Predict")

st.divider()

if predictbutton:
    
    if fuel_type =="CNG":
        fuel_type=0
    elif(fuel_type=="Diesel"):
        fuel_type=1
    else:
        fuel_type=2        
        
        
    if transmission=="Automatic":
        transmission=0
    else:
        transmission=1
    
                
    
    X=[year,km_driven,fuel_type,transmission,owner]
    
    X1=np.array(X)
    
    X_array=scaler.transform([X1])
    
    prediction = model.predict([X1])[0] 
      
    st.balloons()
    
    st.write(f"Predicted Result: {prediction}")
    
    
else:
    st.write("Please enter the values and use predict button")    



