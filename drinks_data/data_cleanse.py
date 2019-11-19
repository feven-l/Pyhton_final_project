import csv
import re


#   Function creates a list of objects for each drink and assigns an ID number for each to be used for python data modelling but not necessary for Django
def read_file(fileName):
    drink_list = []
    with open(fileName, newline='') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        drink_id = 0
        for row in reader:
            ingredients = []
            drink_name = row[0]
            glassType = row[2]
            for num in range(4,10,1):
                if row[num]:
                    ingredients.append({'name': row[num], 'amount': row[num +7]})
            instructions = row[10]
            drink_list.append({'id':drink_id,'name': drink_name, 'glassType': glassType, 'ingredients': ingredients, 'instructions': instructions})
            drink_id +=1
    return drink_list
    



