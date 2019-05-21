
#1、忘记缩进
magicians = ['alice','david','carolina']
for magician in magicians:
print(magician+':你的表演真的是太精彩了！！！')

#2、忘记缩进额外的代码行
magicians = ['alice','david','carolina']
for magician in magicians:
     print(magician+':你的表演真的是太精彩了！！！''.\n')
print('Thank You,'+magician.title()+'小宝贝')

#3、不必要的缩进
message = "Hello Python world!"
    print(message+':你的表演真的是太精彩了！！！')
#4、循环后不必要的缩进
magicians = ['alice','david','carolina']
for magician in magicians:
     print(magician+':你的表演真的是太精彩了！！！')
     print('让我们再次期待'+magician.title()+'下次的经常表演吧！！''.\n')
     print('Thank You,'+magician.title()+'小宝贝')

#5、遗漏了冒号
magicians = ['alice','david','carolina']
for magician in magicians
     print(magician+':你的表演真的是太精彩了！！！')
     print('让我们再次期待'+magician.title()+'下次的经常表演吧！！''.\n')
print('Thank You,'+magician.title()+'小宝贝')