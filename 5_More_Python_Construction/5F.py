from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# a:
def f(x):
    return x**2


integral, error = quad(f, 0, 2)
print(f'quad integral of x^2 from 0 to 2 - analytic result: {integral - 2**3 / 3}')


# b:
# quadrature.py
xmax = np.linspace(0, 5, 51)
integral = np.zeros(xmax.size)


def integrand(x):
    return np.exp(-x**2/2)


for i in range(xmax.size):
    integral[i], error = quad(integrand, 0, xmax[i])
plt.plot(xmax, integral)
plt.axhline(color = 'black')
plt.title(r'$f(x_{max})=\int_0^{x_{max}} e^{-x^2/2} dx$')

plt.xlabel(r'$x_{max}$')
plt.ylabel(r'$f(x_{max})$')
plt.show()
