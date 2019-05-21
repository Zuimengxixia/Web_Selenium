'''写入文件'''

filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love new programming.\n")


'''附加到文件，不会删除原来文件内容，附加都原有文件的末尾'''
filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love new programming.\n")