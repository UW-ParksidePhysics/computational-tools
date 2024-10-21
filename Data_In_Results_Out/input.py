import numpy as np


def load_data():
    data_file = r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'
    data_set = np.loadtxt(data_file, delimiter=',')
    #print(data_set)