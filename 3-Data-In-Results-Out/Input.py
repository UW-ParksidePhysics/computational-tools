import numpy as np


data_file = r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'
data_set = np.loadtxt(data_file, delimiter=',')
print(data_set)