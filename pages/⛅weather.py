# Part 1 of Building Weather App 

import streamlit as st
import requests
import json
import streamlit.components.v1 as components

st.header("Weather App")
st.subheader("Exploring Realtime Weather API")

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
	"X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"],
	"X-RapidAPI-Host": st.secrets["X-RapidAPI-Host"]
}

location = st.text_input("Enter the location", "Chennai")

querystring = {"q":{location}}

response = requests.request("GET", url, headers=headers, params=querystring) ## Output: <Response [200]>
result = response.text # Returns the content of the response

if(response.status_code == 400):
    st.error("No location found matching parameter 'q', try searching for a different location.")

else:
    data = json.loads(result)
    col1, col2 = st.columns(2)

    with col1:

        st.write(f'Name: {data["location"]["name"]}')
        st.write(f'Region: {data["location"]["region"]}')
        st.write(f'Country: {data["location"]["country"]}')
        st.write(f'Local Time: {data["location"]["localtime"]}')
        st.metric(label="wind_kph", value= f'{data["current"]["wind_kph"]}')
        st.write(f'Feels like: {data["current"]["feelslike_c"]} ℃')

    with col2: 

        st.write(f'Temp in Celcius: {data["current"]["temp_c"]}')
        st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
        st.write(f'Condition: {data["current"]["condition"]["text"]}')
        st.image(f'http:{data["current"]["condition"]["icon"]}')
        st.metric(label = "Humidity", value = f'{data["current"]["humidity"]}')

    st.info('⛅ Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.')

    components.html(
        """
        <a href="https://www.weatherapi.com/" title="Free Weather API"><img src='//cdn.weatherapi.com/v4/images/weatherapi_logo.png' alt="Weather data by WeatherAPI.com" border="0" target="_blank"></a>
        """
    )
