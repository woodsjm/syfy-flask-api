from flask import Blueprint, request


user = Blueprint('user', 'user', url_prefix='/user')

@user.route('/login', methods=['GET'])
def login():
    return "LOGGED IN"

@user.route('/register', methods=['POST'])
def register():
    print(request)
    add_user()
    return "REGISTERED"

from processes.background import add_user