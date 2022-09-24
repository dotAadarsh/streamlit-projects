import requests
import streamlit as st
import json

st.header("Deepgram OpenAI Whisper Transcription")
st.subheader("Sounds from Apollo Missions")

audio = st.selectbox(
    'Select an audio to transcribe',
    ('JFK: We Choose the Moon with Apollo 11 Launch', 'Apollo 11: Eagle Has Landed', "Apollo 11: That's One Small Step for (a) Man", 'Apollo 12: Cardiac Sim', 'Apollo 12: All Weather Testing', "Apollo 13: Houston, We've Had a Problem"))

if (audio == 'Apollo 11: Eagle Has Landed'):
    data = 'http://www.nasa.gov/mp3/590333main_ringtone_eagleHasLanded_extended.mp3'
elif(audio == "Apollo 11: That's One Small Step for (a) Man"):
    data = 'http://www.nasa.gov/mp3/590331main_ringtone_smallStep.mp3'
elif(audio == 'Apollo 12: Cardiac Sim'):
    data = 'https://www.nasa.gov/mp3/584851main_Apollo-12_Cardiac-Sim.mp3'
elif(audio == 'Apollo 12: All Weather Testing'):
    data = 'Apollo 12: All Weather Testing'
elif(audio == "Apollo 13: Houston, We've Had a Problem"):
    data = 'http://www.nasa.gov/mp3/574928main_houston_problem.mp3'
elif(audio == "JFK: We Choose the Moon with Apollo 11 Launch"):
    data = 'https://www.nasa.gov/mp3/590325main_ringtone_kennedy_WeChoose.mp3'
else :
    data = 'https://www.nasa.gov/mp3/590320main_ringtone_apollo11_countdown.mp3'

st.audio(data, format='audio/mp3')

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

params = {
    'model': 'whisper',
}

json_data = {
    'url': f'{data}',
}

response = requests.post('https://api.deepgram.com/v1/listen', params=params, headers=headers, json=json_data)
st.info(response.json()["results"]["channels"][0]["alternatives"][0]["transcript"])


st.caption('Audio source: NASA')