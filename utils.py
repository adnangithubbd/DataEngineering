import json

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://datatables.net/examples/styling/stripe.html'
employee_list = []
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='stripe')
for employee_data in table.find_all('tbody'):
    rows = employee_data.find_all('tr')

for row in rows:
    name = row.find_all('td')[0].text
    position = row.find_all('td')[1].text
    offic = row.find_all('td')[2].text
    age = row.find_all('td')[3].text
    start_date = row.find_all('td')[4].text
    salary = row.find_all('td')[5].text
    employee_list.append({
        'Name': name,
        'Position': position,
        'Office': offic,
        'Age': age,
        'Start_date': start_date,
        'Salary': salary
    })

# df = pd.DataFrame(employee_list)
# df.to_csv('my_employee_data2.csv')
# print("Data stored in a csv file ")
# with open('Employee_data','w') as json_file:
#     json.dump(employee_list,json_file,indent=2)
