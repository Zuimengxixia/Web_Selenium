# coding:utf-8

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://mail.163.com/")

driver.implicitly_wait(30)

# 切换iframe

# iframe = driver.find_element_by_tag_name("iframe")

# driver.switch_to_frame(iframe)

# driver.switch_to_frame("x-URS-iframe")

driver.switch_to.frame("x-URS-iframe1543895436222.2554")

driver.find_element_by_name("email").send_keys("qaqzz5123")

driver.find_element_by_name("password").send_keys("hlx951118nb")

# 释放iframe，重新回到主页面上

driver.switch_to.default_content()