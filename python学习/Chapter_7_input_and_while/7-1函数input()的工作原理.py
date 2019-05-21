'''
#input()的简单示例
prompt = "某某某."
prompt += "name? "    #用 += 将多行提示拼接成一条提示

message = input(prompt)
print('Hello,'+ message +"!")
'''
'''
#用int()来获取数值输入
prompt = "我来输入."
prompt += "一个数值? "

message = input(prompt)
print(message)  #因为input()输入的数值保存在message中式字符串形式
message = int(message)  #用int()将字符串视为数值
print(message>=18)   #成功进行数值对比
'''
'''
#实际例子,判断一个人是否满足坐过山车的身高要求：
height = input('请输入您的身高：')
height = int(height)

if height >= 175:
    print('\n不好意思！您的身高太高，不适合')
else:
    print('\n来吧！！兄dei')
'''
#求模运算符
height = input('请输入您的身高：')
height = int(height)

if height % 3 ==0:
    print('\n不好意思！您的身高太高，不适合')
else:
    print('\n来吧！！兄dei')