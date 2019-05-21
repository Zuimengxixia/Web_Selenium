'''列表的传递'''
def greet_users(names):
    for name in names:
        msg = "你好鸭！ "+name.title()+" !"
        print(msg)
username =["hhhhh","aaaaa","wwdssdd"]
greet_users(username)

'''在函数中修改列表'''
def print_models(unprinted_designs,completed_models):    #定义函数 print_models 并包含两个形参

    while unprinted_designs:                 #循环需要打印的 unprinted_designs 列表
        current_design = unprinted_designs.pop()   #逐一删除
        print("\nPrinting model :"+current_design)
        completed_models.append(current_design)  #将删除的值附加给 completed_models
def show_completed_models(completed_models):     #定义函数 show_completed_models 包含形参 completed_models
    print("\n显示所有的模型：")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["ssssssss","wwsdwwds","wwffsss"]  #需要修改的列表
completed_models = []                                  #空列表

print_models(unprinted_designs[:],completed_models)  #调用的时候 unprinted_designs[:] 不清空之前的列表，清空的是副本文件
show_completed_models(completed_models)
print(unprinted_designs)