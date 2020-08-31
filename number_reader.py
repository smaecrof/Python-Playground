# Author: Spencer Mae-Croft
# Date: 08/31/2020 


import json

filename = 'numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object)

print(str(numbers))
