from flask import Flask, request, jsonify
from app.bot.bot import OpenAI
import os

app = Flask(__name__)

bot = OpenAI(
    base_url="https://api.openai.com",
    api_key=str(os.getenv("SECRET_KEY"))
)

@app.route("/", methods=["GET"])
def index():
    return "Olá, bem vindo ao bot da OpenAI!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Mensagem não fornecida'}), 400
    
    response = bot.get_chat(data['message'])
    return jsonify({'response': response})

if __name__ == '__main__':
   app.run(debug=True)
