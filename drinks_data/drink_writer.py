import csv
import json
from data_cleanse import read_file



def prepare_output():
    drink_list = read_file('drinks_data_edited.csv')
    id=1
    output_list = []
    for drink in drink_list:
        drink_dictionary = {
        "model": "apps.drink",
        "pk": id,
        "fields": {
            "name": drink['name'],
            "glassType": drink['glassType'],
            "instructions": drink['instructions']
        }}
        output_list.append(drink_dictionary)
        id +=1
    return output_list


if __name__=='__main__':
    output_list=prepare_output()
    with open('drink.json', 'w') as file_to_write:
        json.dump(output_list, file_to_write)