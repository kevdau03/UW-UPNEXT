from flask import Flask, jsonify, request
from flask_cors import CORS
import json 
from gemini_services import handle_user_prompt

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Endpoint to handle user prompt
@app.route('/api/user_prompt', methods=['POST'])
def user_prompt():
    data = request.get_json()
    prompt = data['message']
    response = handle_user_prompt(prompt)
    return jsonify({'message': response})  # Ensure the response is correctly structured

if __name__ == '__main__':
    app.run(debug=True)