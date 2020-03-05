from flask import Blueprint, Flask
from database.config import create_db
from routes.user import user
from routes.api import api

import os
import sys

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'randomstringxyxzyz'

#db = create_db(app)

# from routes.user import user
# from routes.api import api
db = create_db(app)

app.register_blueprint(user)
app.register_blueprint(api)

@app.route('/')
def index():
    return 'SERVER WORKING'


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
    