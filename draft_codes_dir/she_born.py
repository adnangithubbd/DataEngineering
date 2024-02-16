import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
import numpy as np

# first = random.normal(loc=50, scale=5, size=1000)
# second = random.binomial(n=100, p=0.5, size=1000)
#
# sns.distplot(first,hist=False,label='normal',color='green')
# sns.distplot(second,hist=False,label='binomial',color='red')

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
# plt.show()
# sns.distplot(random.uniform(size=1000),hist=False,color='black')

# sns.distplot(random.uniform(size=100),hist=False,color='pink')

#todo colors
colors = np.array(
    ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
     "magenta"])
#todo sizes
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

# todo first
x = np.random.randint(2, 17, size=13)
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
y = random.randint(np.min(y), np.max(y), size=13)
plt.scatter(x, y, color=colors)

# todo second
x = np.random.randint(2, 17, size=13)
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
y = random.randint(np.min(y), np.max(y), size=13)
plt.scatter(x, y, color=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.grid()
plt.show()
