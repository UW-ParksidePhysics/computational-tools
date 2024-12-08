# a: x_step = 2*x_step - 1
# b: x_position = np.cumsum(x_step) or x_position = x_step.cumsum()
# c:
# random_walk.py
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import random as rng
num_steps = 500
x_step = rng(num_steps) > 0.5
y_step = rng(num_steps) > 0.5
x_step = 2*x_step - 1
y_step = 2*y_step - 1
x_position = np.cumsum(x_step)
y_position = np.cumsum(y_step)
plt.plot(x_position, y_position)
plt.axis('equal')
plt.show()
