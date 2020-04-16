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
        escaped_password = urllib.parse.quote_plus(password)
        MONGO_URL = f'mongodb+srv://{username}:{escaped_password}@syfy-cluster-cpjop.gcp.mongodb.net/test?retryWrites=true&w=majority'
        mongo = MongoClient(MONGO_URL)

        return mongo
