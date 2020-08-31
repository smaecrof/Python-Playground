# Author: Spencer Mae-Croft
# Date: 08/31/2020

flag = True

print("Provide two numbers to be divided!")
print("Enter 'q' or 'Q' to quit the program")

while(flag): 
    first_number = input("\nFirst Number: ")

    if first_number.lower() == 'q':
        flag = False 
        continue

    second_number = input("\nSecond Number: ")

    if second_number.lower() == 'q':
        flag = False
        continue

    try:
        division_Result = int(first_number) / int(second_number)
        print(first_number + "/" + second_number + " = " + str(division_Result))
    
    except ZeroDivisionError:
        print("Cannot divide by zero")


print("Out of the while loop")
