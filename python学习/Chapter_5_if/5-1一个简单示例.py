#通过if判断对汽车名全大写打印
cars = ('audi','bmw','subaru','toyota')
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())