#打印消息，再用切片来打印列表前三个元素
players = ['charles','martina','michael','florence','eli']
print('The first three items in the list are:')
print(players[0:3])

#打印中间三个元素
players = ['charles','martina','michael','florence','eli']
print('\nThree items from the middle of the list are:')
print(players[1:4])

#打印后面三个元素
players = ['charles','martina','michael','florence','eli']
print('\nThe last three items in the list are:')
print(players[2:])

#在原来的列表中添加一个元素
players = ['charles','martina','michael','florence','eli']
players.append('cannoli')
print('\nThe last three items in the list are:')
print(players)

for player in players:
    print(player)