'''
#用while循环从1数到5
a = 1
while a <= 5:
    print(a)
    a +=1
'''
'''
prompt = "我来输入."
prompt += "一个值? "
a = ''
while a != 'quit':
    a = input(prompt)

    if a != 'quit':
        print(a)
'''
'''
prompt = "我来输入."
prompt += "一个值? "
active = True   #让程序开始处于活动状态
while active:
    message = input(prompt)

    if message == 'quit':   #判断当值为quit时，True变为False，循环结束
        active=False
    else:
        print(message)
'''

#使用break退出循环
prompt = "我来输入."
prompt += "一个值? "

while True:   #以True打头的循环将不断的运行
    city = input(prompt)
    if city == 'quit':
        break   #遇到break跳出循环
    else:
        print(city)

'''
#在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number%2==0:   #满足条件跳过继续执行循环，直到完成循环
        continue
    print(current_number)
'''
