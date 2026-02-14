import streamlit as st
import pandas as pd
import joblib

# -------- CUSTOM BACKGROUND STYLE --------
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 Hyderabad House Price Prediction")

st.write("Enter house details")

washrooms = st.number_input("Washrooms", value=2.0)
tennants = st.number_input("Tennants", value=2.0)
area = st.number_input("Area (sqft)", value=1200.0)

if st.button("Predict Price"):

    input_data = pd.DataFrame(
        [[washrooms, tennants, area]],
        columns=['Washrooms','Tennants','Area']
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
