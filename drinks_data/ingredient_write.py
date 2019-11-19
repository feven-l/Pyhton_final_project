from data_cleanse import read_file
import csv

drink_list = read_file('drinks_data_edited.csv')

ingredient_list=[]
for drink in drink_list:
    for ingredient in drink['ingredients']:
        if ingredient['name'] not in ingredient_list:
            ingredient_list.append(ingredient['name'])
id= 0
with open('ingredient_model_data.csv', 'w', newline='') as csvfile_ingredient:
    ingredient_writer = csv.writer(csvfile_ingredient, delimiter =',')
    ingredient_writer.writerow(['id']+ ['ingredient'])
    for ingredient in ingredient_list:
        ingredient_writer.writerow([id,ingredient])
        id +=1
    