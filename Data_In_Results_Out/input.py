import numpy as np


def load_data():
    data_file = r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'
    data_set = np.loadtxt(data_file, delimiter=',')

    return data_set

if __name__ == '__main__':
    test_data_set = load_data()
    print(test_data_set)

    #print(data_set)