from flask import Blueprint, Flask

import os

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.secret_key = 'randomstringxyxzyz'

@app.route('/')
def index():
    return 'SERVER WORKING'


if __name__ == '__main__':
    app.run(debug = DEBUG, port = PORT)