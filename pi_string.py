# Author: Spencer Mae-Croft
# Date: 08/31/2020


filename = "pi_digits.txt"


with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)


pi_string = ""

for line in lines:
    pi_string += line.rstrip()


print(pi_string)










