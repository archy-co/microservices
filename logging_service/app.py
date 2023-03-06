from flask import Flask, jsonify, request

app = Flask(__name__)
messages = {}

@app.route('/', methods=['POST'])
def log_message():
    message = request.json['message']
    m_uuid = request.json['uuid']
    messages[m_uuid] = message
    print(f'{m_uuid}: {message}')
    return f'{m_uuid}: {message}'

@app.route('/', methods=['GET'])
def get_messages():
    return ",".join(messages.values())

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
