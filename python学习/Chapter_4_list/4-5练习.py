#将五个元素放入一个元组里，并用for循环打印出来
floos = ('鸡腿','月饼','粽子','鸡翅','炸鸡')
for floo in floos:
    print(floo)

#修改元组中的一个元素，确定Python会报错
'''
floos = ('鸡腿','月饼','粽子','鸡翅','炸鸡')
floos[0]=('鸡腿子')
'''
#修改元组中的元素，并重新用for打印出来
floos = ('鸡腿','月饼','粽子','鸡翅','炸鸡')
for floo in floos:
    print(floo)

floos = ('鸡腿子','月饼','粽子','鸡中翅','炸火鸡')
for floo in floos:
    print(floo)