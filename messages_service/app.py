from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_message():
    return 'Implemented and working fine'

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
