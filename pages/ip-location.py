import streamlit as st
import requests

# Get the IP address of the current user
response = requests.get("https://ipinfo.io/ip")
ip_address = response.text.strip()

st.write(ip_address)
