#字典列表
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#使用range()生成30个外星人
aliens = []

#创建30个绿色的外星人，用到了range()函数
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print('Total number of aliens: '+str(len(aliens)))

#在字典中储存列表
#将信息都存储在pizza字典中 存储所点披萨的信息
pizza = {
    'crust':'thick',
    'toppomgs':['mushrooms','extra cheese'],  #toppomgs键关联 ['mushrooms','extra cheese'] 列表
}
#概述所点的披萨
print("You ordered a "+ pizza['crust']+ '-crust pizza '+
      "with the following toppings")

for topping in pizza['toppomgs']: #用for循环访问 toppomgs配料列表 ，从中提取配料
    print("\t"+topping)



#在字典中一个键关联多个值
favorite_languages = {
    'jen':['python','c'],
    'sarah':['c++'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite language are:")
    for language in languages:
        print("\t" + language.title())

#在字典中存储字典
users = {                                #先定义一个users的字典并包含俩个键aeinstein和mcurie并各自关联一个字典
    'aeinstein':{                             #其中包含用户的名，姓和地址
        'first': 'albert',
        'last' : 'einstein',
        'location':'princeton',
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for usernaem,user_info in users.items():
    print("\nUsername:"+ usernaem)
    full_name = user_info['first'] + " "+ user_info['last']
    location = user_info['location']

    print("\tFull name:"+ full_name.title())
    print("\tLocation:"+location.title())