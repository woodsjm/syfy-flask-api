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
        print("===================")
        print("INSIDE CREATE DB")
        print("===================")
        #escaped_username = urllib.parse.quote_plus(username)
        escaped_password = urllib.parse.quote_plus(password)

        connection_string = os.environ.get('DATABASE_CONNECTION_STRING')

        #colon = urllib.parse.quote_plus(':')
        url_base = f'mongodb:+srv//{username}:'
        MONGO_URL = url_base + escaped_password + connection_string
        print("MONGO_URL: ", MONGO_URL)
        mongo = MongoClient(MONGO_URL)

        return mongo
