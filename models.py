import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load local .env if running locally
load_dotenv()

# Check Streamlit Cloud secrets first, fall back to environment variable
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def gemini(text):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=text
    )
    return response.text