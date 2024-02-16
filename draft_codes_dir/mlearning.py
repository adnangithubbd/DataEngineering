import numpy as np
import matplotlib.pyplot as plt

speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

x = np.std(speed)
a = np.random.normal(170, 10, 250)
b = np.random.uniform(5, 1, 100000)

plt.hist(a,100)
plt.show()