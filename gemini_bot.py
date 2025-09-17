from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # Load .env file
API_KEY = os.getenv("AIzaSyC1rncWI8tC5If86WxKz9lmWKUbJGHH_Eg")  # Get the key

genai.configure(api_key=API_KEY)
