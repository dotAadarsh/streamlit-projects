import requests
import streamlit as st
import json
from annotated_text import annotated_text
import pandas as pd
import numpy as np

st.header("Air Quality Index")
st.caption("The below result is based on your IP address geolocation")


AQI_API_KEY = st.secrets["AQI_API_KEY"]
url = f"http://api.airvisual.com/v2/nearest_city?&key={AQI_API_KEY}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
result = response.text

location = [[ data["data"]["location"]["coordinates"][1] , data["data"]["location"]["coordinates"][0]]]
df = pd.DataFrame(location, columns=['lat', 'lon'])

st.map(df, zoom=14)

st.info(data["data"]["city"] + ", " + data["data"]["state"] + ", " + data["data"]["country"])
st.metric(label="US AQI", value = data["data"]["current"]["pollution"]["aqius"], help = "US AQI")  

annotated_text(
    ("Good", "0-50", "#2e6930"),
    "   ",
    ("Moderate", "51-100", "#cbb02a"),
    "   ",
    ("Unhealthy for Sensitive Groups", "101-150", "#ff6f00"),
    "   ",
    ("Unhealthy", "151-200", "#e60026"),
    "   ",
    ("Very Unhealthy", "201-300", "#4a2b7a"),
    "   ",
    ("Hazardous", "301+", "#746062"),
    "   "
)


