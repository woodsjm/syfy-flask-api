from flask import Blueprint, jsonify, send_file, request
import requests


api = Blueprint('api', 'api', url_prefix='/api')

# ------------ Get Images for Main Feed ------------
@api.route('/images', methods=['GET'])
def retrieve_images():
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
    print("hitting download")
    imgOptions = request.get_json()

    source, target = None, None
    if imgOptions:
        source = imgOptions['source']
        target = imgOptions['target']
    try:
        secure_url = grab_transformed_image(imgOptions['target'], imgOptions['source'])
    except:
        status = {"code": 400, "message": "ERROR"}
        return jsonify(data={}, status=status) 
    else:
        status = {"code": 200, "message": "OK"}
        return jsonify(data=secure_url, status=status)
        #return jsonify(data=secureUrl, status={'code': 200, 'message': 'OK'})
    
    
from processes.background import grab_image_data, grab_transformed_image