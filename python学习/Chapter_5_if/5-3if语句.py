#一、简单的if语句

#假设有一个表示某人的年龄的变量，判断该年龄是不是符合投票的年龄
age = 19
if age >= 18:
    print('符合投票年龄！')
'''
#二、if-else语句
ages = ('sad','sada')
for age in ages:
    if age == 'sad':
        print(age+',符合投票年龄！')
    else:
        print(age+",对不起，你的年龄不符合要求")


#三、判断列表是否为空
ages = ['dsad','wdsa']
if ages:
    for age in ages:
        print('Adding,'+age+'.')
    print('\nyour pizza!')
else:
    print('nonono')
'''
#四、使用多个列表
available_toppings = ['charles','martina','michael','florence','eli']

requested_toppings = ['charles','weddsa','martina']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding,'+requested_topping+'.')
    else:
        print('对不起，没有这个配料,'+requested_topping)
print('\ndsadsdwasdasd')