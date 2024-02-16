import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15, 12])
labels = ['apples', 'bananas', 'cherries', 'jackfruits', 'mango']
colors = ['red', 'yellow', 'purple', 'green', 'hotpink']
myexplode = [0.1, 0.12, 0.29, 0, 0]

plt.pie(y, labels=labels, colors=colors, explode=myexplode)
plt.show()
