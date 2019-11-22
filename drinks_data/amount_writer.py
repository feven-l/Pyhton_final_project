import data_cleanse
import drink_writer
import ingredient_write
import json


drink_list = drink_writer.prepare_output()
ingredient_list = ingredient_write.prepare_output()
complete_list = data_cleanse.read_file('drinks_data_edited.csv')

ingredient_dictionary = {}
drink_dictionary = {

pairs =[{
    
        "drink": 1,
        "ingredient": 1,
        "amount": "1 oz "
    }
, {
    
        "drink": 1,
        "ingredient": 2,
        "amount": "1 oz "
    
}, {
    
        "drink": 1,
        "ingredient": 3,
        "amount": "1/2 oz "
}, {
    
        "drink": 1,
        "ingredient": 4,
        "amount": "1 dash "
    }
, {
    
        "drink": 2,
        "ingredient": 2,
        "amount": "1 cl "
    }
, {
    
        "drink": 2,
        "ingredient": 5,
        "amount": "4 oz "
    }
, {
    
        "drink": 2,
        "ingredient": 6,
        "amount": "1/4 cl "
    }
, {
    
        "drink": 3,
        "ingredient": 7,
        "amount": "1 oz "
    
}, {
    
        "drink": 3,
        "ingredient": 8,
        "amount": "1/2 oz "
    
}, {
    
        "drink": 3,
        "ingredient": 9,
        "amount": "2 oz "
    
}, {
    
        "drink": 4,
        "ingredient": 10,
        "amount": "3-Jan"
    
}, {
    
        "drink": 4,
        "ingredient": 11,
        "amount": "3-Jan"
   
}, {
    
        "drink": 4,
        "ingredient": 12,
        "amount": "4-Jan"
    
}, {
   
        "drink": 5,
        "ingredient": 13,
        "amount": "1 1/2 oz "
    
}, {
    
        "drink": 5,
        "ingredient": 14,
        "amount": "1 tblsp "
    
}, {
    
        "drink": 5,
        "ingredient": 15,
        "amount": "1"
    
}, {
    
        "drink": 5,
        "ingredient": 16,
        "amount": "1 1/2 oz "
    
}, {
    
        "drink": 5,
        "ingredient": 17,
        "amount": "1 tsp "
    
}, {
    
        "drink": 5,
        "ingredient": 18,
        "amount": "1"
    
}, {
    
        "drink": 6,
        "ingredient": 19,
        "amount": "1 part Bass pale "
    
}, {
    
        "drink": 6,
        "ingredient": 20,
        "amount": "1 part "
    
}, {
    
        "drink": 7,
        "ingredient": 21,
        "amount": "1 1/2 oz "
    
}, {
    
        "drink": 7,
        "ingredient": 22,
        "amount": "3 oz "
    
}, {
    
        "drink": 7,
        "ingredient": 4,
        "amount": "1 dash "
    
}, {
    
        "drink": 7,
        "ingredient": 23,
        "amount": "1/2 tsp "
    
},  {
        "drink": 7,
        "ingredient": 24,
        "amount": "2-3 drops "
    }
, {
        "drink": 7,
        "ingredient": 25,
        "amount": "1 wedge "
    
}, {
        "drink": 8,
        "ingredient": 26,
        "amount": "1 oz "
    
}, {
        "drink": 8,
        "ingredient": 27,
        "amount": "1 oz white "
    
}, {
        "drink": 8,
        "ingredient": 28,
        "amount": "1 oz "
    
}, {
        "drink": 8,
        "ingredient": 29,
        "amount": "\n"
    
}, {
        "drink": 9,
        "ingredient": 13,
        "amount": "2 oz "
    
}, {
        "drink": 9,
        "ingredient": 25,
        "amount": "Juice of 1/2 "
    
}, {
        "drink": 9,
        "ingredient": 30,
        "amount": ""
    
}, {
    
        "drink": 10,
        "ingredient": 13,
        "amount": "1 1/2 oz "
    
}, {
        "drink": 10,
        "ingredient": 25,
        "amount": "Juice of 1/2 "
    
}, {
        "drink": 10,
        "ingredient": 31,
        "amount": "1 tsp "
    
}, {
        "drink": 11,
        "ingredient": 21,
        "amount": "70ml/2fl oz"
    
},  {
        "drink": 11,
        "ingredient": 32,
        "amount": "1 tbsp"
    
}, {
        "drink": 11,
        "ingredient": 33,
        "amount": "2 tbsp"
    
},  {
        "drink": 11,
        "ingredient": 34,
        "amount": "1 wedge"
    
}, {
        "drink": 11,
        "ingredient": 35,
        "amount": "1"
    
}, {
        "drink": 12,
        "ingredient": 36,
        "amount": "1 1/2 oz "
    
}, {
        "drink": 12,
        "ingredient": 17,
        "amount": "2 tsp superfine "
    
}, {
        "drink": 12,
        "ingredient": 4,
        "amount": "1 1/2 oz "
    
},  {
        "drink": 12,
        "ingredient": 37,
        "amount": "4 oz Chilled "
    
}, {
        "drink": 12,
        "ingredient": 38,
        "amount": "1"
    
}, { 
        "drink": 12,
        "ingredient": 39,
        "amount": "1"
    
}, {
        "drink": 13,
        "ingredient": 36,
        "amount": "2 oz "
    
},  {
        "drink": 13,
        "ingredient": 40,
        "amount": "5 oz "
    
}, {
        "drink": 13,
        "ingredient": 25,
        "amount": "1"
    
}, {
        "drink": 14,
        "ingredient": 41,
        "amount": "3/4 oz "
    
}, {
        "drink": 14,
        "ingredient": 27,
        "amount": "3/4 oz white "
    
}, {
        "drink": 14,
        "ingredient": 28,
        "amount": "3/4 oz "
    
}, {
        "drink": 15,
        "ingredient": 21,
        "amount": "1 oz "
    
},  {
        "drink": 15,
        "ingredient": 42,
        "amount": "1/2 oz "
    
}, {
        "drink": 15,
        "ingredient": 5,
        "amount": "4 oz "
    
},  {
        "drink": 16,
        "ingredient": 43,
        "amount": "1 1/2 shot "
    
},  {
        "drink": 16,
        "ingredient": 44,
        "amount": "1 1/2 shot "
    
},  {
        "drink": 16,
        "ingredient": 34,
        "amount": "Juice of 1 wedge "
    
}, { 
        "drink": 17,
        "ingredient": 13,
        "amount": "1 oz "
    
},  {
        "drink": 17,
        "ingredient": 45,
        "amount": "1/2 oz "
    
}, {
        "drink": 17,
        "ingredient": 14,
        "amount": "1/2 oz "
    }
, {
        "drink": 17,
        "ingredient": 46,
        "amount": "1 1/2 oz "
    
},  {
        "drink": 17,
        "ingredient": 18,
        "amount": "1"
    
}, {
        "drink": 18,
        "ingredient": 47,
        "amount": "3/4 oz "
    
}, {
        "drink": 18,
        "ingredient": 48,
        "amount": "2 1/2 oz Blended "
    
},  {
        "drink": 18,
        "ingredient": 49,
        "amount": "dash "
    
}, {
        "drink": 18,
        "ingredient": 50,
        "amount": "2 or 3 "
    
},  {
        "drink": 18,
        "ingredient": 39,
        "amount": "1"
    
}, {
        "drink": 18,
        "ingredient": 51,
        "amount": "1 twist of "
    
},  {
        "drink": 19,
        "ingredient": 52,
        "amount": "1 1/2 oz "
    
}, {
        "drink": 19,
        "ingredient": 14,
        "amount": "1/2 oz "
    
},  {
        "drink": 19,
        "ingredient": 16,
        "amount": "1 oz "
    
}, {
        "drink": 19,
        "ingredient": 53,
        "amount": ""
    
},  {
        "drink": 20,
        "ingredient": 37,
        "amount": "Chilled "
    
}, {
        "drink": 20,
        "ingredient": 5,
        "amount": "2 oz "
    
}, {
        "drink": 21,
        "ingredient": 13,
        "amount": "2-3 oz "
    
}, {
        "drink": 21,
        "ingredient": 25,
        "amount": "Juice of 1 "
    
},  {
        "drink": 21,
        "ingredient": 17,
        "amount": "2 tsp "
    
}, {
        "drink": 21,
        "ingredient": 54,
        "amount": "4-Feb"
    
}, {
        "drink": 21,
        "ingredient": 55,
        "amount": ""
    
}, {
        "drink": 22,
        "ingredient": 21,
        "amount": "2 oz "
    
}, {
        "drink": 22,
        "ingredient": 16,
        "amount": "2 oz "
    
},  {
        "drink": 22,
        "ingredient": 56,
        "amount": "8 oz "
    
},  {
        "drink": 23,
        "ingredient": 13,
        "amount": "3 oz "
    
},  {
        "drink": 23,
        "ingredient": 57,
        "amount": "3 tblsp "
    
}, {
        "drink": 23,
        "ingredient": 58,
        "amount": "3 tblsp "
    
},  {
        "drink": 24,
        "ingredient": 59,
        "amount": "2 oz "
    
},  {
        "drink": 24,
        "ingredient": 4,
        "amount": "1 oz "
    
},  {
        "drink": 24,
        "ingredient": 17,
        "amount": "1-2 tblsp "
    
},  {
        "drink": 24,
        "ingredient": 50,
        "amount": ""
    
},  {
        "drink": 25,
        "ingredient": 60,
        "amount": "2 oz "
    
}, {
        "drink": 25,
        "ingredient": 44,
        "amount": "1/2 oz "
    
},  {
        "drink": 25,
        "ingredient": 4,
        "amount": "1 oz "
    
},  {
        "drink": 26,
        "ingredient": 52,
        "amount": "2 measures "
    
},  {
        "drink": 26,
        "ingredient": 5,
        "amount": ""
    
},  {
        "drink": 26,
        "ingredient": 6,
        "amount": ""
    
},  {
        "drink": 27,
        "ingredient": 36,
        "amount": "2 oz "
    
},  {
        "drink": 27,
        "ingredient": 4,
        "amount": "1 oz "
    
},  {
        "drink": 27,
        "ingredient": 17,
        "amount": "1 tsp superfine "
    
},  {
        "drink": 27,
        "ingredient": 61,
        "amount": "3 oz "
    
}, {
        "drink": 27,
        "ingredient": 39,
        "amount": "1"
    
},  {
        "drink": 27,
        "ingredient": 38,
        "amount": "1"
    
}]


for pair in pairs:
    drink = Drink.objects.get(id=pair['drink'])
    ing = Ingredient.objects.get(id=pair['drink'])
    Amount.objects.create(drink=drink, ingredient=ing)
    








































# if __name__=='__main__':
    
#     with open('amount.json', 'w') as file_to_write:
#         json.dump(output_list, file_to_write)
