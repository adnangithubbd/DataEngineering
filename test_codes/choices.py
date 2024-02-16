import pandas as pd
import numpy as np
from random import choices

arr = np.array([1, 2, 3, 4, 5, 6])
another = choices(arr,k=3)
print(another)
