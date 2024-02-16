import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_corporate_profits_and_losses'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
sortable = soup.find_all('table', class_="wikitable sortable")

first_table_data = []
first_table = sortable[2]
rows_first = first_table.find_all('tr')
for row in rows_first:
    cells = row.find_all(['td', 'th'])
    row_data = [cell.get_text(strip=True) for cell in cells]
    first_table_data.append(row_data)

df = pd.DataFrame(first_table_data)
df.to_csv('Third_table_profit.csv', index=True)

# todo find all table


for single_table in sortable:
    # Find all rows within the current table
    rows = single_table.find_all('tr')

    # Iterate over each row and print the content
    for row in rows:
        # Extract data from each cell in the row
        cells = row.find_all(['td', 'th'])
        row_data = [cell.get_text(strip=True) for cell in cells]

