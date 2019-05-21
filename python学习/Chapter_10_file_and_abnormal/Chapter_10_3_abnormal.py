'''使用try-except处理 ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero！")
'''

'''使用try-except-else处理 ZeroDivisionError异常'''
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit." )

while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input("Second_number: ")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0 !")
    else:
        print(answer)