'''传递任意数量的实参'''
def make_pizza(*toppings):
    '''打印用户所需要的所有配料'''
    print(toppings)
make_pizza("pepperoni")
make_pizza('dddddd','sdsdsdsd','wdsdadad')


def make_pizza(*toppings):
    '''打印用户所需要的所有配料'''
    print("打印用户所需要的所有配料:")
    for topping in toppings:
        print('- '+topping)

make_pizza("pepperoni")
make_pizza('dddddd','sdsdsdsd','wdsdadad')

'''结合使用位置实参和任意数量实参'''
def make_pizza(size,*toppings):              #一个*号 创建空元组
    print("\n这是你要的尺寸："+str(size)+" -with the folowing toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza(15,"ssssssss")
make_pizza(55,"sdsadadasda","wdsdwadas","wfasdasd")

'''使用任意数量的关键字实参'''
def build_profile(first,last,**user_info):   #两个*号 创建空字典
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key,value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('xiaoxiao','cccc',localhsot = "pass",filed = 'word')

print(user_profile)