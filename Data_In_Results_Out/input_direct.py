#import_numpy.py
data_file = r'C:\Users\bleac\PycharmProjects\computational-tools\pmls-data\pmls-data\01HIVseries\HIVseries.csv'
my_file = open(data_file)
temp_data = []
for line in my_file:
    print(line)
    x, y = line.split('.')
    temp_data += [float(x), float(y)]
my_file.close()
#data_set = np.array(temp_data)
print(temp_data)