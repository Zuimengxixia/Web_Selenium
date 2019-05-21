'''有时候一个页面上有多个对象需要操作，如果一个个去定位的话，比较繁琐，这时候就可以定位一组对象。
webdriver 提供了定位一组元素的方法，跟前面八种定位方式其实一样，只是前面是单数，这里是复数形式：find_elements '''

from selenium import webdriver
import random
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("测试部落")
driver.find_element_by_id("kw").submit()  #submit()相当于回车键
l = driver.find_elements_by_css_selector("h3.t>a")
t = random.randint(0,9)
l[t].click()  #前面那种方法，是直接访问url地址，算是接口测试的范畴了，真正模拟用户点击行为，得用click的方法
'''
a = l[t].get_attribute("href")
print(a)
driver.get(a)
'''
'''
 获取href属性 并打印出url地址
for i in l:
    print (i.get_attribute("href"))    
 '''
