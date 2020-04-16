import os
from mongoengine import connect


class Config(object):
    MONGO_URL = 'mongodb://localhost:27017/syfy'
    MONGO_URI = MONGO_URL
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'randomstringzyzx'
