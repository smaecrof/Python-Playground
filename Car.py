# Author: Spencer Mae-Croft
# Date: 08/31/2020


class Car():
    """Representing a simple car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        """Return a neatly formatted descriptive car name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    
    def read_odometer(self):
        """Print a statement describing the car's odometer reading"""
        print("This car as " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self, mileage):
        """Updating the mileage odometer reading if simple requirements are passed"""
        if(mileage > 0 and mileage > self.odometer_reading):
            self.odometer_reading = mileage
        

my_car = Car("Honda", "Civic Hatchback EX" , 2018)
print(my_car.get_description())
my_car.read_odometer()
my_car.update_odometer(33)
my_car.read_odometer()
my_car.update_odometer(32)
my_car.read_odometer()
my_car.update_odometer(31356)
my_car.read_odometer()





class ElectricCar(Car):
    """Represents aspects of a car in a specific way"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make,model,year)


my_tesla = ElectricCar("tesla", "model S", 2018)
print(my_tesla.get_description())



