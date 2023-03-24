import streamlit as st 
from deepgram import Deepgram
import asyncio, json
from fpdf import FPDF
import base64
from itranslate import itranslate as itrans


st.set_page_config(page_title='Aurable', page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)

st.header("Aurable")
st.subheader("One stop place for audio analysis")

st.info("Please enter Deepgram API to proceed!. Get you DG Key [here](https://console.deepgram.com/signup)")
DEEPGRAM_API_KEY = st.text_input("Please enter Deepgram API")

uploaded_file = st.file_uploader("Upload any audio file", type='mp3')
st.info("Upload a audio file. Here is an example audio - [Spacefacts.mp3](./assets/space_facts.mp3)")
PATH_TO_FILE = uploaded_file

with st.sidebar:
    with st.expander("Audio properties"):
        st.write(uploaded_file)

st.audio(uploaded_file)

if uploaded_file:
    async def main():
        # Initializes the Deepgram SDK
        deepgram = Deepgram(DEEPGRAM_API_KEY)
        if PATH_TO_FILE:
            source = {'buffer': uploaded_file, 'mimetype': 'audio/wav'}
            response = await deepgram.transcription.prerecorded(source, {'detect_topics': True, 'detect_language': True, 'summarize': True, 'punctuate': True})
            result = json.dumps(response, indent=4)
            transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
            detected_language = response["results"]["channels"][0]["detected_language"]
            duration = response["metadata"]["duration"]
            confidence = response["results"]["channels"][0]["alternatives"][0]["confidence"]
            summary = response["results"]["channels"][0]["alternatives"][0]["summaries"][0]["summary"]
            total_word = response["results"]["channels"][0]["alternatives"][0]["summaries"][0]["end_word"]
            
            with st.expander("Extracted Transcript"): 
                st.write(transcript)

            with st.expander("Translate the transcript"):
                st.info("Tamil - ta, Russian - ru, German - de, Japanese - ja [More lang will be added]")
                options = st.selectbox("Select the language", ("ta", "ru", "de", "ja"))
                st.text_area("Translated Text", itrans(transcript, to_lang = options))

                
            with st.sidebar:
                with st.expander("Additional Analysis"):

                    st.write(f"Detected Language: {detected_language}")
                    st.write(f"Total Duration: {duration}")
                    st.write(f"Confidence: {confidence}")
                    st.write(f"Total words: {total_word}")

            with st.expander("Summary"):
                st.write(summary)
            
            with st.expander("PDF Converter"): 

                report_text = transcript
                export_as_pdf = st.button("Export Report")

                def create_download_link(val, filename):
                    b64 = base64.b64encode(val)  # val looks like b'...'
                    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

                if export_as_pdf:
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font('Arial', '', 12)
                    pdf.write(5, report_text)
                    
                    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

                    st.markdown(html, unsafe_allow_html=True)

    asyncio.run(main())
