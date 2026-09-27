import streamlit as st
import joblib
import pandas as pd

model = joblib.load("../models/delivery_time_model.joblib")

st.title("Delivery Time Predictor")

distance_km = st.number_input("Distance (km)", min_value=0.0, max_value=25.0, value=5.0)
traffic = st.selectbox("Traffic", ["Low", "Medium", "High", "Jam"])
weather = st.selectbox("Weather", ["Sunny", "Cloudy", "Fog", "Stormy", "Sandstorms", "Windy"])
city = st.selectbox("City", ["Urban", "Metropolitian", "Semi-Urban"])
vehicle = st.selectbox("Vehicle type", ["motorcycle", "scooter", "electric_scooter", "bicycle"])
vehicle_condition = st.selectbox("Vehicle condition", [0, 1, 2, 3])
rating = st.number_input("Delivery person rating", min_value=1.0, max_value=5.0, value=4.6, step=0.1)
multiple_deliveries = st.selectbox("Multiple deliveries", [0, 1, 2, 3])
is_peak_hour = st.selectbox("Peak hour?", ["No", "Yes"])

if st.button("Predict"):
    row = pd.DataFrame([{
        "Delivery_person_Ratings": rating,
        "Road_traffic_density": traffic,
        "multiple_deliveries": multiple_deliveries,
        "Weatherconditions": weather,
        "City": city,
        "Type_of_vehicle": vehicle,
        "Vehicle_condition": vehicle_condition,
        "distance_km": distance_km,
        "is_peak_hour": 1 if is_peak_hour == "Yes" else 0,
    }])
    pred = model.predict(row)[0]
    st.success(f"Estimated delivery time: {pred:.1f} minutes")