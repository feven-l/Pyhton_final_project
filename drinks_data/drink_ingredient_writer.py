import csv
from data_cleanse import read_file

# This creates a many-to-many relationship between drinks and ingredients using drink_id and ingredient name.


# Create the list of drink objects by calling the function read_file
drink_list = read_file('drinks_data_edited.csv')

with open('drink_ingredient_model_data.csv', 'w', newline='') as csvfile_ingredient:
    ingredient_writer = csv.writer(csvfile_ingredient, delimiter =',')
    ingredient_writer.writerow(['drink_id']+ ['ingredient'])
    for row in drink_list:
        for ingredient in row['ingredients']:
            ingredient_writer.writerow([row['id'], ingredient['name']])