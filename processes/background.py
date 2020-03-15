import requests

from credentials.auth import name, key, secret
from utils.image_api import ImageApi


image_api = ImageApi(name, key, secret)

def update_image_data(mongo):
    code, reason, images = image_api.fetch_image_data()
    if code == 200:
        try:
            db = mongo.db
            coll = db['images']
            store_images = coll.insert(images)
        except:
            return "Failed"
        else:
            docs = []
            for doc in store_images:
                docs.append(doc)
            return "Success"
        
