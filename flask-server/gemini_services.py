import google.generativeai as genai

API_KEY = "AIzaSyAnWA58Y4NpDY-rss-LQphg2oyPUxqAgd8"
genai.configure(api_key=API_KEY)
   # Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def handle_user_prompt(prompt):
    #call RAG using the user prompt (returns an array of JSON)
    data = RAG(prompt)

    #gemini responds
    gemini_prompt = f"data is {data} which represents events, extracts the events' location, post URL, time, date."
    response = model.generate_content(gemini_prompt)
    return response

