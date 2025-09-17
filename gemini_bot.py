from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # Load .env file
API_KEY = os.getenv("YOUR_GEMINI_API_KEY")  

genai.configure(api_key=API_KEY)
