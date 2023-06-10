from flask import Flask, request, jsonify
from app.controllers.message_controller import MessageController

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_message():
    data = request.get_json()
    if data and 'message' in data:
        message = data['message']
        response = MessageController.process_message(message)
        return jsonify(response)
    return jsonify({'error': 'Invalid request'})

if __name__ == '__main__':
    app.run()