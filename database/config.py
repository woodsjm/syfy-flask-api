from flask_pymongo import PyMongo 
from pymongo import MongoClient

import os
import sys

def create_db(app):
    MONGO_URL = "mongodb://localhost:27017/syfy"
    app.config['MONGO_URI'] = MONGO_URL
    mongo = PyMongo(app)
    print("HITTING SYFY TEST")
    return mongo
