#使用range()函数
for value in range(1,6):
    print(value)

#使用range()函数创建数字列表
nuwbers = list(range(1,6))
print(nuwbers)

even_nuwber = list(range(1,10,1))
print(even_nuwber)

#多次方算法
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#统计列表的数值
digits = [1,2,3,4,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析,可以将三四行代码合成一行，效果一致
squares = [value**2 for value in range(1,11)]
print(squares)