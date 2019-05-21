'''创建Dog类'''
class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        print(self.name.title() + "roll over!")
'''创建实例调用Dog类方法'''

my_dog = Dog("wilie ",22)
print("我的小狗的名字： "+my_dog.name.title()+" .")
print("我的小狗的年龄： "+str(my_dog.age)+" .")
my_dog.sit()
'''创建多个实例'''
you_dog = Dog("lisa ",12)
print("\n我的小狗的名字： "+you_dog.name.title()+" .")
print("我的小狗的年龄： "+str(you_dog.age)+" .")
you_dog.roll_over()