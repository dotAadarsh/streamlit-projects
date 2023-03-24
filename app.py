import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Streamlit projects", page_icon=None,
                   layout="centered", initial_sidebar_state="expanded", menu_items=None)

st.header("Building projects with streamlit")
st.info("More projects to come! Under construction!!!")
st.image("https://media.giphy.com/media/hvN3SkNMRSB7mZa8JL/giphy.gif")

st.markdown("""
| Title | Blog |
|-------------------------------------------|:----------------------------------------------------------------------------------------:|
| You can just turn data scripts into apps! | [↗](https://aadarshkannan.hashnode.dev/you-can-just-turn-data-scripts-into-apps) |
| Building QR Code generator | [↗](https://aadarshkannan.hashnode.dev/building-qr-code-generator) |
| #01 Lets create a simple weather App | [↗](https://aadarshkannan.hashnode.dev/lets-create-a-simple-weather-app-part-1) |
| real-time live dashboard | [↗](https://blog.streamlit.io/how-to-build-a-real-time-live-dashboard-with-streamlit/) |

""")

with st.expander("Socials"):
    st.markdown('''
            [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dotaadarsh)
            [![Twitter](https://img.shields.io/badge/twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/dotaadarsh)
            [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dotaadarsh/)
            [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/dotaadarsh/)
            [![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/Jj8xeWpnEe)
            [![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)](https://open.spotify.com/user/w4vmhygkyyzefhe1u3bpqrlo6)
            ''')
with st.expander('Buy me a coffee'):
    components.html('''
                <script 
                type="text/javascript" 
                src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" 
                data-name="bmc-button" 
                data-slug="aadarshk" 
                data-color="#5F7FFF" 
                data-emoji=""  
                data-font="Lato" 
                data-text="Buy me a coffee" 
                data-outline-color="#000000" 
                data-font-color="#ffffff" 
                data-coffee-color="#FFDD00" ></script>''', height=100)
