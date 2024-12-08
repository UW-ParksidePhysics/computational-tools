# a:
from scipy.integrate import quad
def f(x): return x**2
integral, error = quad(f, 0, 2)
print(integral - 2**3 / 3)


# b:
# quadrature.py
import numpy as np
from scipy.integrate import quad
xmax = np.linspace(0, 5, 51)
integral = np.zeros(xmax.size)
def integrand(x): return np.exp(-x**2/2)
for i in range(xmax.size):
    integral[i], error = quad(integrand, 0, xmax[i])
plt.plot(xmax, integral)
plt.show()
