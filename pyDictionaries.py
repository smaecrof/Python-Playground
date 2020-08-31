# Author: Spencer Mae-Croft
# Date: 08/31/2020

dean = {
    'first_name': "Dean",        
    'last_name': "Colvin",
    'age': '69',
    'hometown': "Plyouth",
    'state':"Indiana",
    'occupation':"Judge",
}

for key, value in dean.items():
    print("\nKey: " + key + " ------> " + value)

    
    
spencer = {
        'first_name': 'Spencer',
        'last_name': 'Mae-Croft',
        'age': '22',
        'hometown':'Plymouth',
        'state':'Indiana',
        'occupation': 'Programmer'
}

elise = {
        'first_name':'Elise',
        'last_name':'Patrick',
        'age':'22',
        'hometown':'Plymouth',
        'state':'Indiana',
        'Occupation':'Medical School Student'
}


people = [dean, spencer, elise]

for person in people:
    print("\n")
    for key,value in person.items():
        print(key + " ---> " + value)


        



