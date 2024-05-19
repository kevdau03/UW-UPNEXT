from flask import Flask, jsonify, request
from flask_cors import CORS
import json 
from apify_client import ApifyClient

# init an app instance in Flask
app = Flask(__name__)
CORS(app)

# default endpoint
@app.route('/')
def home():
    return "Welcome to the Flask REST API!"

@app.route('/api/user_prompt', methods=['POST'])
def user_prompt():
    data = request.get_json()
    print(data)
    
    #response_data= {'message': 'Your message has been processed!'}
    return jsonify(data)  # Use jsonify for JSON responses


if __name__ == '__main__':
    app.run(debug=True)
