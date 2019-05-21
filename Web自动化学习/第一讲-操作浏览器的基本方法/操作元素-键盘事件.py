'''Selenium2+python自动化12-操作元素（键盘和鼠标事件）'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
time.sleep(1)
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(1)
driver.find_element_by_id("kw").clear()
time.sleep(1)
driver.find_element_by_id("kw").send_keys("隔壁老王")
driver.find_element_by_id("kw").send_keys(Keys.ENTER) # 键盘回车事件
'''
其它常见的键盘操作：

键盘F1到F12：send_keys(Keys.F1) 把F1改成对应的快捷键

复制Ctrl+C：send_keys(Keys.CONTROL,'c') 

粘贴Ctrl+V：send_keys(Keys.CONTROL,'v') 

全选Ctrl+A：send_keys(Keys.CONTROL,'a') 

剪切Ctrl+X：send_keys(Keys.CONTROL,'x') 

制表键Tab:  send_keys(Keys.TAB) 

这里只是列了一些常用的，当然除了键盘事件，也有鼠标事件
'''
