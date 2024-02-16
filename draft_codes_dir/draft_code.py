from bs4 import BeautifulSoup
from random import choices
from scipy import stats

numbers = [2, 3, 4, 5, 6, 7]
squared = {n ** 2 for n in numbers}
squared2 = [n ** 2 for n in numbers]
another = []
for x in range(len(numbers) - 1):
    another.append(numbers[x] ** 2)

one = [1, 2, 3, 4, 5, 2]

two = {1, 2, 3, 4, 5, 2}

# todo strip demo

html = "<td>   Example   </td>"
soup = BeautifulSoup(html, 'html.parser')
cell_text = soup.td.get_text(strip=True)

# todo
ls = [1, 2, 3, 4, 5, 6, 3]
res = {n ** 3 for n in ls}

x, y, z = 12, 2, 3
print(x, y, z)
