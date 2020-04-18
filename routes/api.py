from flask import Blueprint, jsonify, request
import requests

import sys


api = Blueprint('api', 'api', url_prefix='/api')

# ------------ Get Images for Main Feed ------------
@api.route('/images', methods=['GET'])
def retrieve_images():
    print("Hitting retrieve_images")
    sys.stdout.flush()
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
    imgOptions = request.get_json()
    source, target, dev_h, dev_w = None, None, None, None
    # Refactor so request parsed in process
    if imgOptions:
        source = imgOptions['source']
        target = imgOptions['target']
        dev_h = imgOptions['devH']
        dev_w = imgOptions['devW']
    try:
        secure_url = grab_transformed_image(target, source, dev_h, dev_w)
    except:
        status = {"code": 400, "message": "ERROR"}
        return jsonify(data={}, status=status) 
    else:
        status = {"code": 200, "message": "OK"}
        return jsonify(data=secure_url, status=status)
    
    
from processes.background import grab_image_data, grab_transformed_image