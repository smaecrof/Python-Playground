# Author: Spencer Mae-Croft
# Date: 08/31/2020

import json 

numbers = [1,2,3,4,5,6,22,11,13,17] 

filename = 'numbers.json'

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

