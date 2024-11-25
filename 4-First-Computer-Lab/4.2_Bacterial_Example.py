import numpy as np
import matplotlib.pyplot as plt


# Time range
t = np.linspace(0, 3, 100)


# Define parameters for each W function
all_parameters = {
1: {'A':1.0, 'tau': 1},
2: {'A':0.5, 'tau': 0.8},
3: {'A':1.5, 'tau': 1.2},
}


# Define W1, W2, and W3 with their respective parameters
def W(time, amplitude, time_constant):
    return amplitude * (np.exp(-time/time_constant) -1 + time/time_constant)


for index, parameters in all_parameters.items():
    plt.plot(t, W(t, parameters['A'], parameters['tau']))

#Plot W1, W2, W3
#plt.plot(t, W1, linestyle = 'solid', label=r"$W_1(t) = A_1  t$")
#plt.plot(t, W2, linestyle = 'dashed', label=r"$W_2(t) = A_2  t^2$")
#plt.plot(t, W3, linestyle = 'dashdot', label=r"$W_3(t) = A_3  y^3$")


plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Bacterial Growth ($W$)')
plt.title('Bacterial Growth Rate')


plt.legend()
plt.grid(True)
plt.show()

