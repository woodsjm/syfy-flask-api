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
        app.config['MONGO_URI'] = MONGO_URL
        mongo = PyMongo(app)

        return mongo
    
    # HEROKU CONFIG
    else:
        print("===================")
        print("INSIDE CREATE DB")
        print("===================")
        print("USERNAME: ", username)
        print("PASSWORD: ", password)
        escaped_username = urllib.parse.quote_plus(username)
        escaped_password = urllib.parse.quote_plus(password)

        print("ESCAPED USERNAME: ", escaped_username)
        print("ESCAPED PASSWORD: ", escaped_password)

        connection_string = os.environ.get('DATABASE_CONNECTION_STRING')

        print("CONNECTION STRING: ", connection_string)

        test_url = os.environ.get('DATABASE_URL')
        #MONGO_URL = 'mongodb://' + escaped_username + ':' + escaped_password + connection_string
        mongo = MongoClient(test_url)

        return mongo
