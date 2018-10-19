#!/home/developer/Documentos/4Linux/python_fundamentals/venv/bin/python3

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return print(datetime.now().strftime('%d-%m-%Y'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)