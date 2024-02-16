import pandas as pd
import json

with open('sample.json', 'r') as file:
    load_data = json.load(file)
df = pd.DataFrame(load_data)

population = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Population_Millions': [8.4, 3.9, 2.7, 2.3],
    'Area_SqMiles': [468.9, 468.7, 227.3, 637.5]}

cities_df = pd.DataFrame(population)
pop_pivot=pd.pivot_table(cities_df,values='Population_Millions',index='City',
                         columns='Area_SqMiles', aggfunc='sum',fill_value=0)
print(pop_pivot)



con = cities_df[cities_df['Area_SqMiles'] < 3]

area = cities_df[cities_df['Area_SqMiles'] < 500]
areas = area['Population_Millions'].tolist()

total = 0
for value in areas:
    total += value
