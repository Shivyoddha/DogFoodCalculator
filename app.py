import streamlit as st
import json

def calculate_food(activity, weight):
    if activity and weight:
        calculated_amount = round(activity / weight, 2)
        return {"recommendedFood": calculated_amount}
    else:
        return {"error": "Please provide both activity level and weight."}

# Define Streamlit app as a function
def app():
    # Parse JSON data from the POST request
    try:
        data = st.json_request()
        activity = data.get("activity")
        weight = data.get("weight")
    except:
        st.json({"error": "Invalid JSON data"})
        return
    
    # Calculate recommended food
    result = calculate_food(activity, weight)
    
    # Respond with the result as JSON
    st.json(result)

# Run the Streamlit app
if __name__ == "__main__":
    app()
