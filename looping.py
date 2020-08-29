# Author: Spencer Mae-Croft
# Date: 08/29/2020


#numbers = []
#for num in range(1,21):
#    numbers.append(num)
#print(str(numbers))


#numbers = []
#for num in range(1,1000001):
#    numbers.append(num)

#print(str(numbers)) 
#print("Min() numbers: " + str(min(numbers))) 
#print("Max() numbers: " + str(max(numbers)))
#print("Sum() numbers: " + str(sum(numbers))) 

oddNumbers = []
for num in range(1,20):
    if(num % 2 != 0):
        oddNumbers.append(num)
print("\nOdd numbers between 1-20:")
print(str(oddNumbers))


multiplesOfThree = []
for num in range(3,31):
    if(num % 3 == 0):
        multiplesOfThree.append(num)
print("\nMultiples of three:")
print(str(multiplesOfThree))


firstTenCubes = []
for num in range(1,11):
    firstTenCubes.append(num**3)

print("\nFirst ten cubes: ")
print(firstTenCubes)


tenCubes = [num**3 for num in range(1,11)] 
print("\nList comprehension test: \n" + str(tenCubes))
















