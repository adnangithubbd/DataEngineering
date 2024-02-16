from io import BytesIO

import requests
import pandas as pd
import json
from PIL import Image

response = requests.get("https://dummyjson.com/products/1")
print(response.status_code)
main_res = response.json()
images = main_res['images']

img = images[0]
img_res = requests.get(img)
picture = Image.open(BytesIO(img_res.content))
picture.show()

print(img)
# if response.status_code == 200:
#     picture = Image.open(BytesIO(img.content))
#     img.show()
# else:
#     print("Failed to load image with status code : ", response.status_code)
with open("product_image.json", "w") as file:
    json.dump(images, file)
df = pd.DataFrame(images)
df['0'] = ""
df.to_csv("image_csv.csv", index=False)
# with open("product.json", "w") as file:
#     json.dump(response.json(), file)
# with open("product.json", 'r') as file:
#     products = json.load(file)
# images=products['images']
# for image in images:
#     print(image)
