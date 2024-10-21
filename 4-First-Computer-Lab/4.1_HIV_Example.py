import numpy as np
import matplotlib.pyplot as plt

from Data_In_Results_Out.input import load_data


load_data()

time = np.linspace(0, 1, 101)
model_parameters = [
    [3, 0, 8, 11],
    [1, 0, 1, 1,],
]
for [A , B, alpha, beta] in model_parameters:
    parameters_label = f'A = {A}, B = {B}, '+r'$\alpha$ = '+f'{alpha},'\
                        +r'$\beta$ = '+f', {beta}'

# B = 0
# A = 3
# alpha = 8
# beta = 11

    viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)

    plt.plot(time, viral_load, label = parameters_label)

plt.legend()
plt.show()

#np.loadtxt r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'

