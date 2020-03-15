import requests


from credentials.auth import name, key, secret
from utils.image_api import ImageApi


image_api = ImageApi(name, key, secret)

def update_image_data(db):
    code, reason, images = image_api.fetch_image_data()
    if code == 200:
        print(images)
    return "working"
