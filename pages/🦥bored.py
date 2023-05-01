import streamlit as st
import requests
import json
import time

st.set_page_config(page_title = "Are you bored?", page_icon = "🦥") # Configures the default settings of the page.

st.header("Are you bored?")
st.subheader("Let's find you something to do")

bored_api_url = "http://www.boredapi.com/api/activity/"
gif_api_url = "https://giphy.p.rapidapi.com/v1/gifs/search"

gif_api_key = st.secrets["gif-api-key"]

headers = {
"X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"],
"X-RapidAPI-Host": "giphy.p.rapidapi.com"
}

random = st.button("random", help="Click the button to generate an activity for you")

if random:

    response = requests.request('GET', bored_api_url)
    result = response.text
    data = json.loads(result)

    activity = data['activity']
    type_of_activity = data['type']
   
    querystring = {"api_key":gif_api_key,"q": activity, "limit": "1"}

    response_gif = requests.request("GET", gif_api_url, headers=headers, params=querystring)
    result_gif = response_gif.text
 
    data = json.loads(result_gif)

    my_bar = st.progress(0)
    for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)
    
    st.markdown(f'### {activity}')
    st.caption(f'Type: {type_of_activity}')

    if(len(data["data"][0]["images"]["original"]["url"]) == None):
        st.image("https://media.giphy.com/media/71WX8U8zZSBO75RARa/giphy.gif")

    else:
        st.image(data["data"][0]["images"]["original"]["url"])
