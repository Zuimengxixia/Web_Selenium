'''
列表
def get_formatted_ame(first_name,last_name,middle_name=''):  #给形参设置一个默认空字符串
    #返回整洁的姓名
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()     #将结果返还给函数调用行

musican = get_formatted_ame("jiem","hendrix")  #将返回的值保存在变量中
print(musican)
musican = get_formatted_ame("jiem","hendrix","lee")   #让实参变得可选
print(musican)
'''
'''
#字典
def build_person(first_name,last_name,age=''):          #使其能够接受可选值
    返回一个字典,其中包含有关一个人的信息
    person = {'first':first_name,"last":last_name}   #键值对
    if age:
        person["age"]=age                    #当函数调用包含这个形参的时候，将值存储到字典中
    return person

musician = build_person("jime","hendrix",age=12)
print(musician)
'''
def get_formatted_ame(first_name,last_name):
    full_name = first_name+ " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to 'quit')") #提示用户怎么结束填写
    f_name = input("First name: ")
    if f_name == "q":       #输入q的时候循环结束
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_ame = get_formatted_ame(f_name,l_name)  
    print("\nHello, "+formatted_ame+"!")