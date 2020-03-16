from flask import Blueprint, jsonify
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
    
from processes.background import grab_image_data