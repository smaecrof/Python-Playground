# Author: Spencer Mae-Croft
# Date: 08/31/2020

from name_function import get_formatted_name 


print("Enter 'q' at any time to quit the application.")

while True:
    first = input("\nPlease enter your first name: ")

    if first.lower() == 'q':
        break

    last = input("\nPlease enter you last name: ") 

    if last.lower() == 'q':
        break

    middle = input"\nPlease enter a middle name (enter blank to void): " 

    if middle:
        formatted_name = get_formatted_name(first, last, middle)
    else:
        formatted_name = get_formatted_name(first,last)

    print("\nNeatly formatted name: " + formatted_name + ".")
