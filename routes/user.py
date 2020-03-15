from flask import Blueprint


user = Blueprint('user', 'user', url_prefix='/user')

@user.route('/login', methods=['GET'])
def login():
    return "LOGGED IN"

@user.route('/register', methods=['POST'])
def register():
    return "REGISTERED"

from webapp import db