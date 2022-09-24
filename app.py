import streamlit as st

st.set_page_config(page_title="Streamlit projects", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)

st.header("Building projects with streamlit")
st.info("More projects to come! Under construction!!!")
st.image("https://media.giphy.com/media/hvN3SkNMRSB7mZa8JL/giphy.gif")

col1, col2 = st.columns(2)

with col1:
    with st.expander("Completed", expanded = True): 
        st.success("1. QR Generator App")
        st.success("2. Weather App")

with col2:
    with st.expander("TO-DO", expanded = True):
        st.info('3. Translation App')
        st.info('4. Geolocation App')
        st.info('5. Bored App')