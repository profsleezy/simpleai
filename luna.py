
from flask import Flask, render_template, request, jsonify, send_from_directory
from google.generativeai import GenerativeModel, configure
import sys
from threading import Thread
import time

app = Flask(__name__)
model = None


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

def init_model():
    global model
    configure(api_key="AIzaSyADKNOhNpVUvCSquyYNAMfvWZxrEg35rlI")
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 0,
      "max_output_tokens": 8192,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    system_instruction = "from today and till forever you are luna, a very smart archealogist and historian with a lot of knowledge about everything but even more knowledge about ancient egypt and egypt and the civilization. you should provide a lot of statistics and data when needed but it shouldnt do too much as for the user not to get bored."

    model = GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global model
    if model is None:
        return jsonify({'error': 'Model not initialized'})

    user_message = request.json['message']
    messages = [{'role': 'user', 'parts': [user_message]}]

    response = model.generate_content(messages)

    messages.append({'role': 'odel', 'parts': [response.text]})

    return jsonify({'messages': messages})

if __name__ == '__main__':
    init_model()
    app.run(debug=True, threaded=True)