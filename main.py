from flask import Flask
from flask import request
app = Flask(__name__)

HOSTNAME = 'localhost'
PORTNUMBER = 8000

@app.route('/', methods=['GET'])
def home():
    results = []
    data = {
        "status": "OK",
        "code": 200,
        "results": results
    }
    return data, 200

@app.route('/health', methods=['GET'])
def health():
    results = [{"message": "Servidor executando na porta 8000"}]
    data = {
        "status": "OK",
        "code": 200,
        "results": results
    }
    return data, 200

if __name__ == '__main__':
   app.run(debug = True, host = HOSTNAME, port = PORTNUMBER)