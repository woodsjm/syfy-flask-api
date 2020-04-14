import requests
from PIL import Image
from flask import send_file
import io


from credentials.auth import name, key, secret
from utils.image_api import ImageApi


image_api = ImageApi(name, key, secret)

# ***FIX: REMOVE AFTER REFACTORING FOR CIRCULAR IMPORTS*** 
def grab_db_session(mongo):
    global db
    db = mongo.db
    update_image_data()
    return

# ------------ Update Images from Cloudinary ------------
# ***FIX: NEED TO MAKE THIS A NIGHTLY PROCESS AFTER DEPLOY***
def update_image_data():
    print("Hitting update_image_data")
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
            if len(inner) == 3:
                image_data.append(inner)
                inner = []
        image_data.append(inner)
        print(image_data)
        return image_data

# MAIN PROCESSES - FIX: REFACTOR BY BREAKING THESE OUT FROM BACKGROUND
def grab_transformed_image(target, source):
    print(source)
    image = image_api.fetch_transformed_cloudinary_img(target, source)
    if image:
        return image  
    else:
        return

def add_user():
    print("Hitting add_user")
    return "Succes"





        
