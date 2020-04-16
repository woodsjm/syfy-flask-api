from flask import Blueprint, Flask
from flask_cors import CORS
from flask_debug import Debug
import os
import sys

from processes.background import grab_db_session
from database.config import create_db
from routes.api import api
from routes.user import user


DEBUG = True
PORT = 8000

app = Flask(__name__)
Debug(app)
app.secret_key = 'randomstringxyxzyz'

# Configure and initialize DB
db = create_db(app)
# Pass DB session to Background Processes Module
grab_db_session(db)

origins = [
    'http://localhost:3000',
    'https://www.syfywallpapers.site',
    'https://www.syfywallpapers.site/',
    'http://www.syfywallpapers.site',
    'http://www.syfywallpapers.site/',
    'www.syfywallpapers.site',
    'www.syfywallpapers.site/',
    'syfywallpapers.site',
    'syfywallpapers.site/'
]

CORS(api, origins=origins, supports_credentials=True)
CORS(user, origins=origins, supports_credentials=True)

app.register_blueprint(user)
app.register_blueprint(api)

@app.route('/')
def index():
    if 'ON_HEROKU' in os.environ:
        return 'HEROKU SERVER WORKING'
    else:
        return 'LOCAL SERVER WORKING'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, use_reloader=False)