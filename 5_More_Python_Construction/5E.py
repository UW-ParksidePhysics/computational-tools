# quadrature.py
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad
import sympy as sp


x_max = np.linspace(0, 3*np.pi, 16)

integral = np.zeros(x_max.size)
for i in range(x_max.size):
    integral[i], error = quad(np.cos, 0, x_max[i])
diff_x = np.diff(x_max)
cos_x = np.cos(x_max)
adjacent_sums = cos_x[:-1] + cos_x[1:]
trapezoid_areas = 0.5 * adjacent_sums * diff_x
print(f'trapezoid_sum: {np.sum(trapezoid_areas)}')
print(f'quad:{integral[-1]}')


x = sp.symbols('x')
analytic_integral = sp.integrate(sp.cos(x), (x, 0, 3*sp.pi))
print(f'analytic result: {analytic_integral}')


plt.plot(x_max, integral)
plt.show()