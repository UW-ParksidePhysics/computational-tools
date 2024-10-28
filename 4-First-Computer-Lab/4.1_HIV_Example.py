import numpy as np
import matplotlib.pyplot as plt


def load_data():
    data_file = r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'
    data_set = np.loadtxt(data_file, delimiter=',')

    return data_set


hiv_data = load_data().transpose()
plt.plot(hiv_data[0], hiv_data[1], marker = 'o', linestyle = 'None' , color = 'red', label = 'HIV Data')

time = np.linspace(0, 8, 101)
model_parameters = [
    [0.7*1.75e5, 0.3*1.75e5, 1/2, 1/3],
    [0.7*1.75e5, 0.3*1.75e5, 1/1.5, 1/3],
    [0.6*1.75e5, 0.4*1.75e5, 1/1.5, 1/3],
]
for [A , B, alpha, beta] in model_parameters:
    parameters_label = f'A = {A:.3e}, B = {B:.3e},\n'+r'$\alpha$ = '+f'{alpha:.2f}, '\
                        +r'$\beta$ = '+f', {beta:.2f}'

    viral_load_A = A * np.exp(-alpha*time)
    viral_load_B = B * np.exp(-beta*time)
    viral_load = viral_load_A + viral_load_B

    plt.plot(
             time, viral_load,
             label = 'Model: \n' + parameters_label)

large_time_label = r'$V(t\gg0) \rightarrow B e^{-\beta t}$'
small_time_label = r'$V(t\sim 0) \rightarrow A e^{-\alpha t}$'

plt.annotate(large_time_label, xy=(time[-1], viral_load[-1]) , xytext = (6, 2.5e4) ,arrowprops=dict(facecolor='black', shrink=0.09, width = 1, headwidth = 5))
plt.annotate(small_time_label, xy=(time[0], viral_load[0]) , xytext = (0.7, 1.7e5), arrowprops=dict(facecolor='black', shrink=0.09, width = 1, headwidth = 5))

latency_period = 10
latency_ratio = latency_period * alpha
plt.text(0.5,3.5e4, r'$T_\text{lat}\alpha =$'+f'{latency_ratio:.2f}')

plt.xlabel('Time (y)')
plt.ylabel('Viral Load')

plt.legend()
plt.show()

#np.loadtxt r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'

