'''9-1、餐馆'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("我的餐厅是： "+self.restaurant_name)
        print("招牌菜式是： "+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+" 正在营业！")

restaurant = Restaurant("hhh","wisk")
restaurant.describe_restaurant()
restaurant.open_restaurant()
