import streamlit as st
import requests

st.title(
    "Groq Agentic AI System"
)

query = st.text_input(
    "Ask a question"
)

if st.button("Search"):

    response = requests.get(
        "http://127.0.0.1:8000/query",
        params={
            "q": query
        }
    )

    st.write(response.json())