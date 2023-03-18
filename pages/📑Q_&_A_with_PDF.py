from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import PointStruct
import pdfplumber
import streamlit as st
import openai 

st.set_page_config(page_title = "Q & A with PDF", page_icon = "📑") # Configures the default settings of the page.

st.set_option('deprecation.showfileUploaderEncoding', False)

# openai.api_key = st.secrets["OPENAI_KEY"]
# QDRANT_HOST = st.secrets["QDRANT_HOST"]
# QDRANT_API_KEY = st.secrets["QDRANT_API_KEY"]

def create_answer_with_context(qdrant_client, query):
    response = openai.Embedding.create(
        input="What is starship?",
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']

    search_result = qdrant_client.search(
        collection_name="qAndAWithPDF",
        query_vector=embeddings, 
        limit=5
    )

    prompt = "Context:\n"
    for result in search_result:
        prompt += result.payload['text'] + "\n---\n"
    prompt += "Question:" + query + "\n---\n" + "Answer:"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
        )

    return completion.choices[0].message.content

def create_index(qdrant_client, points):
    operation_info = qdrant_client.upsert(
    collection_name="qAndAWithPDF",
    wait=True,
    points=points)

    return operation_info

def create_embeddings(chunks):
    points = []
    i = 1
    for chunk in chunks:
        i += 1
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings = response['data'][0]['embedding']

        points.append(PointStruct(id=i, vector=embeddings, payload={"text": chunk}))
    
    return points

def split_into_chunks(text):
    chunks = []
    while len(text) > 500:
        last_period_index = text[:500].rfind('.')
        if last_period_index == -1:
            last_period_index = 500
        chunks.append(text[:last_period_index])
        text = text[last_period_index+1:]
    chunks.append(text)

    with st.expander("Chunks"):
        for chunk in chunks:
            st.write(chunk)
            st.write("---")
    return chunks

def extract_text(uploaded_file):

    fulltext=""
    if uploaded_file:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                fulltext += page.extract_text()

    if fulltext is not None:
        with st.expander("Extracted text"):
            st.write(fulltext)
    
    return fulltext

def main():
    st.header("Question and Answer on your data")
    st.caption("Powered by Qdrant & OpenAI")

    with st.expander("Context", expanded=False):
        st.write("""
        Qdrant (read: quadrant ) is a vector similarity search engine. 
        It provides a production-ready service with a convenient API to store, search, and manage points - vectors with an additional payload. 
        Qdrant is tailored to extended filtering support. 
        It makes it useful for all sorts of neural network or semantic-based matching, faceted search, and other applications.
        - [Question and Answer on your data with Qdrant](https://lablab.ai/t/question-and-answer-on-your-data-with-qdrant)
        - [Qdrant.tech](https://qdrant.tech/)
        - [OpenAI](https://openai.com/)
        """)
        st.info("Get your API keys and enter it to continue!")
        
    with st.sidebar:
        OPENAI_KEY = st.text_input("Please enter the OpenAI API Key")
        QDRANT_HOST = st.text_input("Please enter the Qdrant host key")
        QDRANT_API_KEY = st.text_input("Please enter the Qdrant API Key")
    
    if OPENAI_KEY and QDRANT_API_KEY and QDRANT_HOST:
        
        openai.api_key = OPENAI_KEY
            
        qdrant_client = QdrantClient(
            host=QDRANT_HOST, 
            api_key=QDRANT_API_KEY,
        )

        qdrant_client.recreate_collection(
            collection_name="qAndAWithPDF",
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
        )

        collection_info = qdrant_client.get_collection(collection_name="qAndAWithPDF")
    
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        
        if uploaded_file is not None:
            fulltext = extract_text(uploaded_file)

            if fulltext is not None:
                chunks = split_into_chunks(fulltext)
                points = create_embeddings(chunks)
                operation_info = create_index(qdrant_client, points)
            
            input = st.text_input("Enter your query")

            if input:
                answer = create_answer_with_context(qdrant_client, input)
                st.success(answer)

if __name__ == '__main__':
    main()