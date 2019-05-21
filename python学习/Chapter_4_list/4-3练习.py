#数到20，使用一个for循环打印数字（包含20）
sums = range(1,21)
for suma in sums:
    print(suma)
'''
#创建一个列表，其中包含数字1~1000000，用for打印出来
for sumaa in range(1,1000001):
    print(sumaa)
'''

#创建一个列表1~1000000，使用min()和max()函数，在用sum()函数统计和
squares = []
for value in range(1,1000000):
    square = value**1
    squares.append(square)
print(min(squares))
print(max(squares))
print(sum(squares))

#通过range()指定第三个参数创建列表，打印出1~20之间的奇数
squares = list(range(1,20,2))
print(squares)
for square in squares:
    print(square)

#创建一个列表，其中包含3~30以内能被3整除的数字，并用for打印出来
squares = []
for value in range(1,11):
    square=value*3
    squares.append(square)
print(squares)

#将同一个数字进行立方，并用for打印
squares = []
for value in range(1,10):
    square=value**3
    squares.append(square)
print(squares)

#使用列表解析生成一个列表，包含1~10的整数立方
squares = [value**3 for value in range(1,10)]
print(squares)

