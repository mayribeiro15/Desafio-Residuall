from flask import Flask
from flask import request
import http.client
import mimetypes
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
    valid_syntax = []
    for x in email_adress:
        if(x.endswith('.com') or 
        x.endswith('.com.br') or
        x.endswith('.gov.br') or
        x.endswith('.org')):
            valid_syntax.append(True)
        else:
            valid_syntax.append(False)
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

@app.route('/mail/validation/v3', methods=['POST'])
def mail_validation_api():
    request_data = request.get_json()
    email_adress = request_data['email_adress']
    results = []

    for x in email_adress:
        #Trecho copiado da documentação da API
        conn = http.client.HTTPSConnection("api.eva.pingutil.com")
        payload = ''
        headers = {}
        conn.request("GET", "/email?email="+x, payload, headers)
        res = conn.getresponse()
        ans = res.read()
        results.append(ans.decode("utf-8"))


    data = {
        "status": "OK",
        "code": 200,
        "results": results
    }
    return data

if __name__ == '__main__':
   app.run(debug = True, host = HOSTNAME, port = PORTNUMBER)