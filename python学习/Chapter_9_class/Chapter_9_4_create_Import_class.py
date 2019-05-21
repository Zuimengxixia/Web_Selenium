'''
     一个模块导入多个类
from car.car import Car,ElectricCar
my_new_car = Car("audi", "a4", 2018)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar("tesla","roadster",2018)
print(my_tesla.get_descriptive_name())
'''

import car.car

my_beetle = car.car.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.car.ElectricCar('tesla','roadster',2018)
print(my_tesla.get_descriptive_name())