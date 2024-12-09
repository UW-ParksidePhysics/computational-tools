import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import is needed for 3D plotting

# Generate data
x = np.linspace(-1, 1, 100)  # x-coordinates
y = np.linspace(-1, 1, 100)  # y-coordinates
x, y = np.meshgrid(x, y)     # Create a grid for x and y
z = x**2 + y**2              # Calculate z values based on the function

# Create a figure for 3D plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create the surface plot
surface = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Add color bar for scale
#fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

# Set plot titles and labels
ax.set_title(r"$z = x^2 + y^2$")
ax.set_xlabel( r"$x$")
ax.set_ylabel( r"$y$")
ax.set_zlabel( r"$z$")

# Show the plot
plt.show()

