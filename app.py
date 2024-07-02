from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import openai

load_dotenv()

openai.api_key = os.getenv("API_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@localhost:3306/book_ai_app'

CORS(app)


@app.route('/', methods=['GET'])
def home():
  with open("text.txt", "r") as f:
    transcript = f.read()

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize the following text"},
        {"role": "assistant", "content": "Yes."},
        {"role": "user", "content": transcript}
      ],
    )

    print(response["choices"][0]["message"]["content"])

  return 'Check the console for output'

if __name__ == '__main__':
    app.run(debug=True)
