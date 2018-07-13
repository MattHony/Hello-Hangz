'''
from car import Car
from car import ElectricCar
from car import Car ,ElectricCar
'''

class Car(object):
    def __init__(self,year,model,maker):
        self.year = year
        self.maker = maker
        self.model = model

    def get_descriptive_name(self):
        long_name = self.year+''+self.model+''+self.maker
        return long_name.title()

class ElectricCar(Car):
    def __init__(self,year,model,maker):
        super().__init__(year,model,maker)
        #self.battery = Battery()

my_tesla = ElectricCar('2018','tesla',"models")
print(my_tesla.get_descriptive_name())