import matplotlib.pyplot as plt
from scipy import stats
from scipy import constants
from scipy.optimize import root
from numpy import cos
import numpy as np


def eqn(x):
    return x + cos(x)


myroot = root(eqn, 0)
print(myroot.x)
print(dir(np))
