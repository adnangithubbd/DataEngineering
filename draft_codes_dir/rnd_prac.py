from numpy import random
import numpy as np
import pandas as pd

# todo 100 range, 2-D(3*5)
x = random.randint(100, size=(3, 5))
# todo generate array(1D) of size 20
k = random.randint(20, size=30)

# todo choice randomly from array and make 2D(3*5)
y = random.choice([3, 5, 7, 9], size=(3, 5))

# todo randint(lower,upper,times)
sold = np.random.randint(100, 200, 10)
sold2 = random.randint(100, 200, 10)

# todo
per = np.array([1, 2, 3, 4, 5, 6])
random.shuffle(per)

f = np.random.normal(170, 10, 250)
print(len(f))