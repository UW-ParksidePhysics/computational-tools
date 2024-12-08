# quiver.py
import numpy as np
from matplotlib import pyplot as plt
coords = np.linspace(-1, 1, 11)
X, Y = np.meshgrid(coords, coords)
Vx, Vy = X, -Y
plt.quiver(X, Y, Vx, Vy)
plt.show()

# a) Arrows curve up compared to original
# b) Arrows point away from the center