import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# todo notice
df = pd.read_csv('data.csv')
for row in df.index:
    if df.loc[row, 'Duration'] > 120:
        df.drop(row, inplace=True)

df.to_csv('new_edited_file.csv')
