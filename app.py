from flask import Flask, render_template, request, jsonify
from chatbot.nlu import get_intent
from chatbot.responses import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    intent = get_intent(user_msg)
    bot_reply = get_response(intent, user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
