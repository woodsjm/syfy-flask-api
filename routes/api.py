from flask import Blueprint, jsonify, request
import requests

import json
import sys


api = Blueprint('api', 'api', url_prefix='/api')

# ------------ Get Images for Main Feed ------------
@api.route('/images', methods=['GET'])
def retrieve_images():
    print("Hitting retrieve_images")
    sys.stdout.flush()
    visitor_addr = request.environ['REMOTE_ADDR']
    print("Visitor ip: =====v")
    print(visitor_addr)

    try:
        data = grab_image_data()
    # ***FIX: ADD PROPER EXCEPTION HANDLING FOR FLASK RESPONSE***   
    except: 
        status = {"code": 400, "message": "ERROR"}
        return jsonify(data, status)
    else:
        status = {"code": 200, "message": "OK"}
        return jsonify(data=data, status=status)

@api.route('/download', methods=['POST', 'OPTIONS'])
def download_image():
    print("Hitting download_image")
    sys.stdout.flush()
    
    parsed_json = request.get_json()
    source, transformations = None, None
    if parsed_json:
        source = parsed_json['source']
        transformations = [transformation for transformation in parsed_json['options']]

    try:
        secure_url = grab_transformed_image(source, transformations)
    except:
        status = {"code": 400, "message": "ERROR"}
        return jsonify(data={}, status=status) 
    else:
        status = {"code": 200, "message": "OK"}
        return jsonify(data=secure_url, status=status)
    
    
from processes.background import grab_image_data, grab_transformed_image