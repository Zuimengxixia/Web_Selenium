#切片
players = ['charles','martina','michage','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[-3:])

#遍历切片
players = ['charles','martina','michage','florence','eli']
print('\n'+'My is name：')
for player in players[-3:]:
    print(player.title())

#复制列表
My_foods = ['pizza','falafel','carrot cake']
friend_foods = My_foods[:]
My_foods.append('cannoli')
friend_foods.append('ice cream')

print('\n'+"我喜欢的食品：")
print(My_foods)

print("\n我朋友喜欢的食品：")
print(friend_foods)