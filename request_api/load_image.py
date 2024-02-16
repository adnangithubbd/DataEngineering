from io import BytesIO

import requests
import pandas as pd
import json
from PIL import Image
import os

response = requests.get("https://dummyjson.com/products/")

main_res = response.json()
# images = main_res['images']
products = main_res['products']
save_directory="request_api"
os.makedirs(save_directory,exist_ok=True)

thums = []
for product in products:
    thums.append(product['thumbnail'])

for i, link in enumerate(thums):
    img_res = requests.get(link)
    if img_res.status_code == 200:
        img_content = BytesIO(img_res.content)
        img = Image.open(img_content)
        img.save(os.path.join(save_directory, f"images_{i + 1}.jpg"))
    else:
        print(f"Failed to download images with status code {img_res.status_code}")

# for img_url in images:
#     img_res = requests.get(img_url)
#     picture = Image.open(BytesIO(img_res.content))
#     picture.show()
# print("end of the show")
