import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print(df.iloc[:, :])
x = df['Pulse']
y = df['Maxpulse']

plt.scatter(x,y,label='labels',marker='*',s=30)

plt.xlabel('Pulse')
plt.ylabel('Maxpulse')
plt.show()

