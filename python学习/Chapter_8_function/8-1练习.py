'''
#一、
def make_shirt(chima,yangshi):
    print("能够接受的尺码："+str(chima))
    print("需要印上去的样式："+yangshi)
make_shirt(41,"hh")

#二、
def make_shirt(yangshi="I Love Python",chima="XL"):
    print("\n能够接受的尺码：" + chima)
    print("需要印上去的样式：" + yangshi)
make_shirt()
make_shirt(chima="XXL")
make_shirt(yangshi="papinilini")
'''
def describe_city(csname,ssgj="中国"):
    print(ssgj)
    print(csname)
describe_city(csname="cs")
