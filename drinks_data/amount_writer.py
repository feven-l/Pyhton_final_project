import data_cleanse
import drink_writer
import ingredient_write
import json


drink_list = drink_writer.prepare_output()
ingredient_list = ingredient_write.prepare_output()
complete_list = data_cleanse.read_file('drinks_data_edited.csv')

ingredient_dictionary = {}
drink_dictionary = {}

for item in ingredient_list:
    ingredient_dictionary[item['fields']['name']] = item['pk']

for drink in drink_list:
    drink_dictionary[drink['fields']['name']] = drink['pk']

output_list = []
amount_id = 1

for drink in complete_list:
    for ingredient in drink['ingredients']:
        amount=ingredient['amount']
        amount_dict = {
            'model': "apps.amount",
            'pk': amount_id,
            "fields":{
                "drink": drink_dictionary[drink['name']],
                "ingredient":ingredient_dictionary[ingredient['name']],
                "amount": amount
            }
        }
        output_list.append(amount_dict)
        amount_id +=1


#print(output_list)
#print(complete_list)

if __name__=='__main__':
    
    with open('amount.json', 'w') as file_to_write:
        json.dump(output_list, file_to_write)
