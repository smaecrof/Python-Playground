# Author: Spencer Mae-Croft 
# Date: 08/31/2020

# Representation of a dog class 

class Dog():
    """ A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes/field variables"""
        self.name = name;
        self.age = age; 

    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")


    def roll_over(self):
        """Simulating a dog rolling over in response to a command"""
        print(self.name.title() + " is rolling over")



my_dog = Dog("Herk",14)

print("My dogs name was " + my_dog.name.title())
print("He lived until the age of " + str(my_dog.age))

my_dog.sit(); 
my_dog.roll_over(); 







