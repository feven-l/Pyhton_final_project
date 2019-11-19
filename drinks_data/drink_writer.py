import csv
from data_cleanse import read_file

drink_list = read_file('drinks_data_edited.csv')

with open('drink_model_data.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile, delimiter = ',')
    data_writer.writerow(['id']+['name'] + ['glassType'] + ['instructions'])
   
    for row in drink_list:
        data_writer.writerow([row['id'],row['name'], row['glassType'].lower(), row['instructions']])