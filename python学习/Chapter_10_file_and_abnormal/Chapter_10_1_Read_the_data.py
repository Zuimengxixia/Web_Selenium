'''读取文件'''
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
''''''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


print(pi_string)
print(len(pi_string))
'''