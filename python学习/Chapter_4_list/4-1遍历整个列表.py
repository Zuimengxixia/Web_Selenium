'''用for循环打印列表中的名单'''
magicians = ['alice','david','carolina']
for magician in magicians:
     print(magician+':你的表演真的是太精彩了！！！')
        #for循环中可以多行任意代码，都会逐一执行
     print('让我们再次期待'+magician.title()+'下次的经常表演吧！！''.\n')
     '''由于没有缩进，所以不在for循环中只会执行一次'''
print('Thank You')