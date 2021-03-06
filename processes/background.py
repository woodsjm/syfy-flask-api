import requests
import sys

from credentials.auth import name, key, secret
from utils.image_api import ImageApi


image_api = ImageApi(name, key, secret)

# ***FIX: REMOVE AFTER REFACTORING FOR CIRCULAR IMPORTS*** 
def grab_db_session(mongo):
    global db
    db = mongo.db
    # FIX: MOVE update_image_data() INTO HEROKU BACKGROUND JOB
    update_image_data()
    return

# ------------ Update Images from Cloudinary ------------
# ***FIX: NEED TO MAKE THIS A NIGHTLY PROCESS AFTER DEPLOY***
def update_image_data():
    code, reason, images = image_api.fetch_cloudinary_images()
    if code == 200:
        try:
            coll = db['images']
            store_images_cursor = coll.insert(images)
        # ***FIX: ADD PROPER EXCEPTION HANDLING FOR MONGODB***
        except:
            return "Failed to Add images to DB"
        else:
            return "Success"

def grab_image_data():
    try: 
        coll = db['images']
        image_data_cursor = coll.find({}, {'_id': 0, 'public_id': 1})
    # ***FIX: ADD MORE COMPREHENSIVE EXCEPTION HANDLING FOR MONGODB***
    except:
        return "Failed to Retrieve images from DB"
    else:
        image_data = []
        inner = []
        for doc in image_data_cursor:
            inner.append(doc['public_id'])
            if len(inner) == 8:
                image_data.append(inner)
                inner = [] 
        if len(inner) > 0:
            image_data.append(inner)
        return image_data

# MAIN PROCESSES - FIX: REFACTOR BY BREAKING THESE OUT FROM BACKGROUND
def grab_transformed_image(source, transformations):
    most_recent_source = None
    try:
        coll = db['images']
        image_version = coll.find_one({ 'public_id': source }, { 'version': 1, '_id': 0 })
        most_recent_source = 'v' + str(image_version['version']) + '/' + source
    except:
        most_recent_source = source
    else:
        image = image_api.fetch_transformed_cloudinary_img(most_recent_source, transformations)
        if image:
            return image

def add_user():
    print("Hitting add_user")
    return "Succes"





        
