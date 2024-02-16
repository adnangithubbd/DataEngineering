import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/'
responce = requests.get(url)
print(responce.status_code)
data = responce.json()


with open('json_out.json', 'w') as file:
    json.dump(data, file)

with open('json_out.json', 'r') as file:
    loaded_data = json.load(file)

print(len(loaded_data))
