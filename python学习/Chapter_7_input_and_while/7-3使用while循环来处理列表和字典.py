'''在列表之间移动元素
unconfirmed_usrs = ['wd','ew','ra']   #待认证列表
confirmed_users = []                  #等待赋值的空列表

while unconfirmed_usrs:               #不断运行 unconfirmed_usrs 直到列表数据为空
    ccurrent= unconfirmed_usrs.pop()  #pop()函数 将unconfirmed_usrs列表的数值从后一个一个删除并存储到ccurrent
    print(ccurrent)                   #打印 ccurrent
    confirmed_users.append(ccurrent)  #将已验证的值赋值给 confirmed_users 空列表
print("\n已经验证的用户：")
for bs in confirmed_users:            #用for循环逐一遍历列表
    print(bs)
'''
'''
#删除包含特定值的所有列表元素
a = ["s","d","s","w","s","r"]
while "s" in a:
    a.remove("s")
print(a)
'''
#使用用户输入来填充字典
responses = {}
polling_active = True   #标志
while polling_active:
    name = input("\n你的姓名是？")
    response = input("你好么？")
    responses[name] =response
    repeat = input("\n还有人么？（yes/no）")
    if repeat == "no":
        polling_active = False

print("\n看结果")
for name,response in responses.items():
    print(name+"ddddd"+response)