import requests
from bs4 import BeautifulSoup
import csv
import json
import matplotlib.image as image
import matplotlib.pyplot as plt

url = 'https://oxylabs.io/blog/python-web-scraping'
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
img_tags = soup.find_all('img', recursive=True)
image_links = [img['src'] for img in img_tags if 'src' in img.attrs]
image_alter = [item['alt'] for item in img_tags]
json_data = [{'src': link, 'alt': alt} for link, alt in zip(image_links, image_alter)]
print(type(json_data))

# with open('info.json', 'a', encoding='utf-8') as file:
#     json.dump(json_data, file)
#
# file_path = 'image_links.csv'
# with open(file_path, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Image Links', 'Alt text'])
#     writer.writerows(zip(image_links, image_alter))


i = image.imread('img.jpg')
plot = plt.imshow(i)

