from flask import Blueprint

api = Blueprint('api', 'api', url_prefix='/api')

@api.route('/images', methods=['GET'])
def retrieve_images():
    return 'Retrieving Images'

