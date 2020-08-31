# Author: Spencer Mae-Croft
# Date: 08/31/2020


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    contents = contents.rstrip()
    print(contents)
