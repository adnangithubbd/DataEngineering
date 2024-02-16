import requests
from bs4 import BeautifulSoup
import csv
import requests
import matplotlib.pyplot as plt
import numpy as np

url = 'https://oxylabs.io/blog/python-web-scraping'
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')

img_tags = soup.find_all('img', recursive=True)
print(img_tags[0]['src'])
links = [item['src'] for item in img_tags if 'src' in item.attrs]
image_links = [img['src'] for img in img_tags if 'src' in img.attrs]
print(type(links))






"""
   
# Specify the CSV file name
csv_file = 'image_links.csv'

# Writing image links to CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Image Links'])
    # Write links
    writer.writerows([[link] for link in image_links])

print(f'Image links saved to {csv_file}')


"""
