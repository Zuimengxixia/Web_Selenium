#一个简单的字典样式
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

#使用字典
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print('你获得了'+str(new_points)+'分')

#添加键-值对
alien_0 = {'color':'green','points':5}
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#创建一个空的字典，在添加键-值对
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

#删除键-值对
del alien_0['color']
print(alien_0)


#一个有趣的例子，
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position:"+str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position:"+str(alien_0['x_position']))

#由类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("Sarah's favorite_languages is "+
      favorite_languages['edward'].title()+
      ' .')

#遍历字典
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print('\nkey:'+key)
    print('value:'+value)

#使用name和language变量
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+
          language.title()+'.')

#遍历字典中所有的键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print('\n')
for name in favorite_languages.keys():
    print(name.title())

#
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
if 'erin' not in favorite_languages.keys(): #判断erin这个人是不是存在于favorite_languages 字典里，不在就打印下列语句
    print("\nErin,please take our poll!")
friends = ['phil','sarah']
for name in sorted(favorite_languages.keys()): # sorted() 排序作用
    print(name.title())

    if name in friends:    #打印 favorite_languages 中的所有名字，并检查是否存在 friends中，如果在就打印下列语句
        print("  Hi "+name.title()+
              ', I see you favorite_languages is '+
              favorite_languages[name].title()+'.')
        # 只遍历字典中的所有值
for language in set(favorite_languages.values()):  # set()集合类似于列表，但是每个元素都是独一无二的
    print(language.title())



