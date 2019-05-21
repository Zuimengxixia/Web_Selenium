'''
不是所有的弹出框都叫alert，在使用alert方法前，先要识别出到底是不是alert。先认清楚alert长什么样子，下次碰到了，就可以用对应方法解决。
alert\confirm\prompt弹出框操作主要方法有：
text：获取文本值
accept() ：点击"确认"
dismiss() ：点击"取消"或者叉掉对话框
send_keys() ：输入文本值 --仅限于prompt,在alert和confirm上没有输入框
'''

from selenium import webdriver
import time
url = "file:///C:/Users/Administrator/Desktop/test.html"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(4)
#driver.find_element_by_id("alert").click()
#driver.find_element_by_id("confirm").click()
driver.find_element_by_id("prompt").click()
time.sleep(3)
'''先用switch_to_alert()方法切换到alert弹出框上'''
t =driver.switch_to_alert()
#打印警告框的文本内容
print(t.text)
t.send_keys("hello word!")
#点击弹窗确认按钮
t.accept()
#点击取消或者X关闭弹窗
#t.dismiss()
