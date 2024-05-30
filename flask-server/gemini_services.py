import google.generativeai as genai
from RAG import return_events
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='./secrets.env')
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
   # Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def handle_user_prompt(prompt):
    #call RAG using the user prompt (returns an array of JSON)
    data = return_events(prompt)
    #gemini responds
    gemini_prompt = f"data is {data} which represents events, extracts the events' location, post URL, time, date. Do NOT put them in tables, instead use whitespace and newlines"
    response = model.generate_content(gemini_prompt)
    return response.text

