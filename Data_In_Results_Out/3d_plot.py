# line3d.py
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import axes3d   # Get 3d plotting tool.



t = np.linspace(0, 5*np.pi, 100)
ax = plt.figure().add_subplot(projection='3d')
ax.plot(np.cos(t), np.sin(t), t)

plt.show()
