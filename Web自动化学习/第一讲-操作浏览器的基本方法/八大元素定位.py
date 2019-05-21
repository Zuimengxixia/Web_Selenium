from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("python")    #通过id进行定位 find_element_by_id()

driver.find_element_by_name("wd").send_keys("python")  #通过name进行定位find_element_by_name()

driver.find_element_by_class_name("s_ipt").send_keys("python")  #通过class进行定位 find_element_by_class_name()

driver.find_element_by_tag_name("input").send_keys("python")  #通过tag标签进行定位 find_element_by_tag_name() 由于标签太多一般不用来定位

driver.find_element_by_link_text("hao123").click()    #通过link_text进行定位 find_element_by_link_text()

driver.find_element_by_partial_link_text("ao123").click()   #通过partial_link_text进行模糊匹配定位 find_element_by_partial_link_text()

driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python")    #通过xpath进行定位 find_element_by_xpath()

driver.find_element_by_css_selector("#kw").send_keys("python")    #通过css进行定位 find_element_by_css_selector()