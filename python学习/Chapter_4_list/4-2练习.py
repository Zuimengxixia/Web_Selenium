#写出三种披萨，并用for循环打印出来
foods = ['banana pizza!','apple pizza!','ham pizza!']
for food in foods:
    print(food)

#用for循环造带有食品的句子
foods = ['banana pizza!','apple pizza!','ham pizza!']
print('\n')
for food in foods:
    print('老板！来一份 '+food+'套餐')

#在结尾添加一行不在循环中的的结束语
foods = ['banana pizza!','apple pizza!','ham pizza!']
print('\n')
for food in foods:
    print('老板！来一份 '+food+'套餐')
print('嗯嗯~~这家的披萨味道真心不错！！！')