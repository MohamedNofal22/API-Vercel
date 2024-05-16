from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from g4f.client import Client
from pymongo import MongoClient
import random
from flask_mail import Mail, Message
import string


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

client = Client()

# MongoDB configuration
uri = 'mongodb+srv://asdevlopers02:6fXfDFKNImSUAiKJ@cluster0.us8nw6q.mongodb.net/'

db_client = MongoClient(uri)
db = db_client['user_database']
users_collection = db['users']

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'himanshu.k822887@gmail.com'
app.config['MAIL_PASSWORD'] = 'vqeq nzsi hlzx sohb'
app.config['MAIL_DEFAULT_SENDER'] = 'BrainWave'

mail = Mail(app)

@app.route('/')
def open():
    return 'API Request Success'

@app.route('/generate_response', methods=['POST'])
def generate_response():
    content = request.json.get('content')

    if not content:
        return jsonify({"error": "Content not provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}],
        )
        generated_response = response.choices[0].message.content

        return jsonify({"response": generated_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
