from flask_pymongo import PyMongo 
from pymongo import MongoClient
import os
import sys
import urllib.parse


def create_db(app):
    # Heroku Credentials
    username = os.environ.get('DATABASE_USERNAME')
    password = os.environ.get('DATABASE_PASSWORD')

    # LOCAL CONFIG
    if not username and not password:
        MONGO_URL = 'mongodb://localhost:27017/syfy'
        mongo = MongoClient(MONGO_URL)
        
        return mongo
    
    # HEROKU CONFIG
    else:
        connection_string = os.environ.get('DATABASE_CONNECTION_STRING')
        url = f'mongodb:+srv//{username}:{password}{connection_string}'
        MONGO_URL = urllib.parse.quote_plus(url)
        mongo = MongoClient(MONGO_URL)

        return mongo
