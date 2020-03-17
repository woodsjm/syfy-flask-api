from flask import Blueprint, Flask
from flask_cors import CORS
from flask_debug import Debug
import sys
import os

from processes.background import grab_db_session
from database.config import create_db
from routes.api import api
from routes.user import user


DEBUG = True
PORT = 8000

app = Flask(__name__)
Debug(app)
app.secret_key = 'randomstringxyxzyz'

db = create_db(app)
grab_db_session(db)

CORS(api, origins=['http://localhost:3000'], supports_credentials=True)
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(user)
app.register_blueprint(api)

@app.route('/')
def index():
    return 'SERVER WORKING'


# if __name__ == '__main__':
app.run(debug=DEBUG, port=PORT)