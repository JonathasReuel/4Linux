from flask import Flask, jsonify
from pymongo import MongoClient
import requests

con = MongoClient()

db = con['projeto']

app = Flask(__name__)

@app.route('/')
def index():
    mensagem = {"mensagem":"minha primeira api rest"}
    return jsonify(mensagem)

@app.route('/contas')
def conta():
    return jsonify([x for x in db.conta.find()])

@app.route('/cep/<cep>')
def cep(cep):
    a = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    return jsonify(a.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)