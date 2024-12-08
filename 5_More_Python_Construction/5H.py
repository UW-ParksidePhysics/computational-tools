# quiver.py
import numpy as np
from matplotlib import pyplot as plt
coords = np.linspace(-1, 1, 11)
X, Y = np.meshgrid(coords, coords)
Vx, Vy = Y, -X
plt.quiver(X, Y, Vx, Vy)
plt.show()

# Vortex travels in a clock wise direction