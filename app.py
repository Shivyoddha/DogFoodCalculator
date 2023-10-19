import streamlit as st
import json

@st.cache
def calculate_food(activity, weight):
    if activity and weight:
        calculated_amount = activity / weight
        return {"recommendedFood": calculated_amount}
    else:
        return {"error": "Please provide both activity level and weight."}

st.title("Dog Food Calculator API")

activity = st.slider("Select Activity Level", min_value=0, max_value=200, step=1)
weight = st.slider("Enter Weight (lbs)", min_value=0, max_value=200, step=1)

result = calculate_food(activity, weight)
st.json(result)
