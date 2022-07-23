import streamlit as st
import requests
import json


headers = {
	"X-RapidAPI-Key": "b01c915818msh1ac6223277f1701p10c98bjsn922743827e5a",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

url = "https://weatherapi-com.p.rapidapi.com/current.json"

st.title("Weather App")
st.subheader("Exploring RapidAPI's weather Endpoints")

location = st.text_input("Enter the location", "Chennai")

querystring = {"q":{location}}

response = requests.request("GET", url, headers=headers, params=querystring)

result = response.text

with st.expander("json output"):
    st.json(result)

data = json.loads(result)

col1, col2 = st.columns(2)

with col1:

    st.write(f'Name: {data["location"]["name"]}')
    st.write(f'Region: {data["location"]["region"]}')
    st.write(f'Country: {data["location"]["country"]}')
    st.write(f'Local Time: {data["location"]["localtime"]}')

with col2: 
    st.write(f'Temp in Celcius: {data["current"]["temp_c"]}')
    st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
    st.write(f'Condition: {data["current"]["condition"]["text"]}')
    st.image(f'http:{data["current"]["condition"]["icon"]}')

wind_kph = f'{data["current"]["wind_kph"]}'

st.metric(label="wind_kph", value=wind_kph)

st.info('⛅ Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.')