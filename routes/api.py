from flask import Blueprint, jsonify
import requests

# from credentials.auth import name, key, secret
# from utils.image_api import ImageApi


api = Blueprint('api', 'api', url_prefix='/api')



@api.route('/images', methods=['GET'])
def retrieve_images():
    
    return "working"
    
