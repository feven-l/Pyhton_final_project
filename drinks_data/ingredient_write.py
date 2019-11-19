from data_cleanse import read_file
import json

def prepare_output():
    drink_list = read_file('drinks_data_edited.csv')
    ingredient_list=[]
    for drink in drink_list:
        for ingredient in drink['ingredients']:
            if ingredient['name'] not in ingredient_list:
                ingredient_list.append(ingredient['name'])

    

    id= 1
    output_list = []
    for ingredient in ingredient_list:
        ingredient_dictionary ={
            "model": "testing_data.ingredient",
            "pk": id,
            "fields":{
                "name": ingredient
            }
        }
        id += 1
        output_list.append(ingredient_dictionary)
    return output_list

if __name__=='__main__':
    output = prepare_output()
    with open('ingredient.json', 'w') as file_to_write:
        json.dump(output, file_to_write)