
import streamlit as st
import requests
import json
import time

# Set the title and icon of the Streamlit app
st.set_page_config(page_title="Are you bored?", page_icon="🦥")

# Add a header and subheader to the app
st.header("Are you bored?")
st.subheader("Let's find you something to do")

# Define the API URLs and API keys for the Bored API and GIPHY API
bored_api_url = "http://www.boredapi.com/api/activity/"
gif_api_url = "https://giphy.p.rapidapi.com/v1/gifs/search"
gif_api_key = st.secrets["gif-api-key"]

# Define the headers for the GIPHY API request
headers = {
    "X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"],
    "X-RapidAPI-Host": "giphy.p.rapidapi.com"
    }

# Create a "random" button to generate a new activity
random = st.button("random", help="Click the button to generate an activity for you")

# If the "random" button is clicked...
if random:
    # Make a request to the Bored API and parse the response as JSON
    response = requests.request('GET', bored_api_url)
    result = response.text
    data = json.loads(result)

    # Extract the activity and type of activity from the Bored API response
    activity = data['activity']
    type_of_activity = data['type']

    # Make a request to the GIPHY API with the activity as the search query
    querystring = {"api_key": gif_api_key, "q": activity, "limit": "1"}
    response_gif = requests.request("GET", gif_api_url, headers=headers, params=querystring)
    result_gif = response_gif.text
    data = json.loads(result_gif)

    # Create a progress bar to show the user that the app is loading
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    # Display the activity and type of activity as a Markdown header and caption
    st.markdown(f'### {activity}')
    st.caption(f'Type: {type_of_activity}')

    # If a GIF URL was found for the activity, display the GIF
    # Otherwise, display a default "bored" GIF
    if len(data["data"][0]["images"]["original"]["url"]) == None:
        st.image("https://media.giphy.com/media/71WX8U8zZSBO75RARa/giphy.gif")
    else:
        st.image(data["data"][0]["images"]["original"]["url"])
