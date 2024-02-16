import random
import pandas as pd
import numpy as np
from random import choices
import matplotlib.pyplot as plt


# todo failed due to ai

np.random.seed(10)
n_records = 1000
n_outlets = 10
n_products = 20

dates = pd.date_range(start='2002-5-20', end='2024-2-14')
dates = choices(dates, k=n_records)

outlets = ['outlets_' + str(i) for i in range(n_outlets)]
outlets = choices(outlets, k=n_records)

products = ['Products_ ' + str(i) for i in range(n_products)]
products = choices(products, k=n_records)

units_sold = np.random.randint(1, 200, n_records)
price_per_unit = np.random.uniform(10, 500, n_records)

total_sell = price_per_unit * units_sold

df = pd.DataFrame({
    'Date': dates,
    'Outlet': outlets,
    'Product': products,
    'Unit_sold': units_sold,
    'Price_per_unit': price_per_unit,
    'Total_sell': total_sell
})

print(df.head(10).to_string())
