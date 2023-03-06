from flask import Flask, request
import uuid
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_message():
    logging_messages = requests.get('http://127.0.0.1:5001').text
    messages = requests.get('http://127.0.0.1:5002').text
    return logging_messages + "\n" + messages + "\n"

@app.route('/', methods=['POST'])
def log_message():
    msg = request.json['msg']
    m_uuid = str(uuid.uuid4())
    requests.post('http://127.0.0.1:5001', json={"uuid": m_uuid, "message": msg})
    return "Message logged\n"

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
