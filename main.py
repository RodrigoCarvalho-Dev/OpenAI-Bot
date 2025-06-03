from flask import Flask, request, jsonify
import os
from app.bot.bot import GeminiBot

app = Flask(__name__)

port = int(str(os.getenv("PORT")))

bot = GeminiBot(
    api_key=str(os.getenv("SECRET_KEY"))
)

@app.route("/", methods=["GET"])
def index():
    return "bem vindo ao bot da SechPay"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Mensagem não fornecida'}), 400
    
    response = bot.get_chat(data['message'])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
