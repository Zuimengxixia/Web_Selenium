'''下列编写一个表示汽车的类，它存储有汽车相关的信息'''
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.modle = model
        self.year = year
        '''默认一个初始值为0的属性'''
        self.odometer_reading = 55

    def get_descriptive_name(self):
        long_car = str(self.year)+" "+self.make+" "+self.modle
        return long_car.title()

    def read_odometer(self):
        '''打印一条汽车里程的消息'''
        print("This car has "+str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        '''将里程表数设为指定的值
           禁止里程表读数回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        '''将里程表读数增加指定的量'''
        self.odometer_reading += miles

my_new_car = Car("Audi","A4",2016)
print(my_new_car.get_descriptive_name())
'''方法1、直接修改属性的值
my_new_car.odometer_reading = 23
'''
'''方法2、通过方法修改属性的值'''
my_new_car.update_odometer(100)
my_new_car.read_odometer()

'''方法3、通过方法对属性的值进行递增'''
my_new_car.increment_odometer(100)
my_new_car.read_odometer()