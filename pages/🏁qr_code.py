import streamlit as st

st.set_page_config(page_title = "QR code generator", page_icon = "🏁") # Configures the default settings of the page.

st.title("QR code generator")
st.subheader("About QR Code")

st.markdown(
    """
    QR Code stands for Quick Response Code and is a type of 2D barcode. 
    It was created by the Japanese corporation [Denso Wave](https://www.denso-wave.com/en/) in 1994 and is one of the most popular types of barcodes.
    QR codes are used to store information such as URLs, contact information, and small amounts of text. They are often used to share links to websites or online resources.
    """)

st.video("https://youtu.be/cswo_6kj0Ug")

st.markdown("We will be using [QRTag API](https://www.qrtag.net/api/) for this project.")

size = st.number_input("Size of your QR Code", 5, 30)
img_type = st.radio("Select image type 🖼️", ('png', 'svg'))
web_link = st.text_input("Enter website URL 🔗", value = "https://aadarshkannan.hashnode.dev/")

QRTag_API_URL = f"https://qrtag.net/api/qr_{size}.{img_type}?url={web_link}"

with st.expander("Generated QR Code", expanded = True):
    st.write("Scan 🤳/ Export ↗️ / do whatever you want 👻")
    st.image(QRTag_API_URL)
