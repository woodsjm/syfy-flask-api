from flask import g, Response
import cloudinary
import requests
import sys


class ImageApi:
    def __init__(self, name, key, secret):
        self.name = name
        self.key = key
        self.secret = secret
        
        cloudinary.config(cloud_name=name, api_key=key, api_secret=secret)

    def which_cloud(self):
        print(self.name)

    def fetch_cloudinary_images(self):
        url_list = cloudinary.utils.cloudinary_url("lg.json", type="list")
        print(url_list)
        try:
            response = requests.get(url_list[0])
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
            return [response.status_code, response.reason]
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            return [response.status_code, response.reason]
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            return [response.status_code, response.reason]
        except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else {err}")
            return [response.status_code, response.reason]
        else:
            data = response.json()
            image_data = data["resources"]
            print(image_data)
            return([response.status_code, response.reason, image_data])

    def fetch_transformed_cloudinary_img(self, targetImg, sourceImg):
        # Refactor method arguments
        img_url = cloudinary.CloudinaryImage(targetImg).build_url(effect="style_transfer", flags="attachment", overlay=sourceImg, sign_url=True)
        return img_url

            

