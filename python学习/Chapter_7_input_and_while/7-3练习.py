'''
sandwich_ordwrs = ["app","Android","IPhone"]
finished_sandwichs = []

while sandwich_ordwrs:
    linshi = sandwich_ordwrs.pop()
    print("目前还有的东西："+linshi)
    finished_sandwichs.append(linshi)
print("所有的东西已经做好，如下：")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich)
'''
sandwich_ordwrs = ["app","Android","IPhone","app","pastrami","pastrami"]
while  sandwich_ordwrs:
    input("点点什么？")
    if sandwich_ordwrs == "pastrami":
        print("不好意思，我们店里的“pastrami”都卖完了")
    else:
        break
print("还剩下：")
while "pastrami" in sandwich_ordwrs:
    sandwich_ordwrs.remove("pastrami")
print(sandwich_ordwrs)
