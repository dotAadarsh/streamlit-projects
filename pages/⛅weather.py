import streamlit as st
import requests
import json
import streamlit.components.v1 as components

headers = {
	"X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"],
	"X-RapidAPI-Host": st.secrets["X-RapidAPI-Host"]
}

url = "https://weatherapi-com.p.rapidapi.com/current.json"

st.title("Weather App")
st.subheader("Exploring RapidAPI's weather Endpoints")
option = st.radio("Choose an option", ('real-time', 'history'))

if option == "real-time":

    location = st.text_input("Enter the location", "Chennai")
    querystring = {"q":{location}}
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text

    with st.expander("json output"):
        st.json(result)

    data = json.loads(result)
    col1, col2 = st.columns(2)
    wind_kph = f'{data["current"]["wind_kph"]}'
    humidity = f'{data["current"]["humidity"]}'

    with col1:

        st.write(f'Name: {data["location"]["name"]}')
        st.write(f'Region: {data["location"]["region"]}')
        st.write(f'Country: {data["location"]["country"]}')
        st.write(f'Local Time: {data["location"]["localtime"]}')
        st.metric(label="wind_kph", value=wind_kph)
        st.write(f'Feels like: {data["current"]["feelslike_c"]} C')

    with col2: 

        st.write(f'Temp in Celcius: {data["current"]["temp_c"]}')
        st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
        st.write(f'Condition: {data["current"]["condition"]["text"]}')
        st.image(f'http:{data["current"]["condition"]["icon"]}')
        st.metric(label = "Humidity", value = humidity)

if option == "history":

    st.header("History Weather")
    st.info("History weather API method returns historical weather for a date on or after 1st Jan, 2010 (depending upon subscription level) as json.")

    location = st.text_input("Enter the location", "London")
    date_user = st.date_input("Select the date")
    st.write(date_user)
    hist_url = "https://weatherapi-com.p.rapidapi.com/history.json"
    querystring = {"q":location,"dt": date_user,"lang":"en"}

    response = requests.request("GET", hist_url, headers=headers, params=querystring )

    with st.expander("JSON History", expanded = False):
        st.json(response.text)


st.info('⛅ Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.')

components.html(
    """
    <a href="https://www.weatherapi.com/" title="Free Weather API"><img src='//cdn.weatherapi.com/v4/images/weatherapi_logo.png' alt="Weather data by WeatherAPI.com" border="0" target="_blank"></a>
    """
)