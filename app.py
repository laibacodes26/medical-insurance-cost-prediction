import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Medical Insurance Cost Predictor")

age = st.slider("Age", 18, 64, 30)
gender = st.selectbox("Gender", ["male", "female"])
bmi = st.slider("BMI", 15.0, 55.0, 25.0)
children = st.slider("Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Cost"):
    row = pd.DataFrame({
        'age': [age],
        'gender': [1 if gender == 'male' else 0],
        'bmi': [bmi],
        'children': [children],
        'smoker': [1 if smoker == 'yes' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0]
    })
    result = model.predict(row)[0]
    st.success(f"Estimated Insurance Cost: ${result:.2f}")
