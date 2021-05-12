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

@app.route('/mail/validation/v1', methods=['POST'])
def mail_validation():
    request_data = request.get_json()
    email_adress = request_data['email_adress']
    if(email_adress.endswith('.com') or 
    email_adress.endswith('.com.br') or
    email_adress.endswith('.gov.br') or
    email_adress.endswith('.org')):
        valid_syntax = True
    else:
        valid_syntax = False
    results = {
        "email_adress": email_adress,
        "domain": "mail",
        "valid_syntax": valid_syntax
    }
    data = {
        "status": "OK",
        "code": 200,
        "results": results
    }
    return data

if __name__ == '__main__':
   app.run(debug = True, host = HOSTNAME, port = PORTNUMBER)