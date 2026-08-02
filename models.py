import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize client(access of api)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def gemini(text):
    response = client.models.generate_content(
        model="gemini-3.6-flash",  # <--- Change model here
        contents=text
    )
    return response.text