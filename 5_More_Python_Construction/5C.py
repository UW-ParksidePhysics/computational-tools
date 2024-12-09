#hitogram.py
from matplotlib import pyplot as plt
from numpy.random import random as rng


data = rng(100)
counts, bin_edges, _= plt.hist(data)
plt.hist(data)
plt.show()
