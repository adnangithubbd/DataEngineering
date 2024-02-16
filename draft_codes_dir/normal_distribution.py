import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.normal(170, 10, 250)
sns.distplot(x,hist=False)
plt.show()
