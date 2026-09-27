from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, jsonify
from flask_cors import CORS
from viacep_client import get_address_by_cep

app = Flask(__name__)
CORS(app)

@app.get('/')
def index():
    return jsonify({'service': 'cep_service', 'status': 'ok'})

@app.get('/cep/<cep>')
def get_cep(cep: str):
    address = get_address_by_cep(cep)
    
    if address is None:
        return jsonify({
            'error': 'not_found',
            'message': f'CEP {cep} inválido ou não encontrado'
        }), 404
        
    return jsonify(address), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)