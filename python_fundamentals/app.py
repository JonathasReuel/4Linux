#!/home/developer/Documentos/4Linux/python_fundamentals/venv/bin/python3

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return datetime.now().strftime('%d-%m-%Y')
    jsonify()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)