opened_file = open('testcsv.csv')

from csv import reader
read_file = reader(opened_file)
print(read_file)
apps_data = list(read_file)

print(len(apps_data))
print(apps_data[:5])

