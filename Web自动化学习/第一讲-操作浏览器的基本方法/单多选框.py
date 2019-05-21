from selenium import webdriver

driver = webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/do.html")
'''
ts = driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in  ts:
    i.click()
'''
'''
这里注意，敲黑板做笔记了：find_elements是不能直接点击的，它是复数的，所以只能先获
 取到所有的checkbox对象，然后通过for循环去一个个点击操作
 
 .is_selected()判定选项框状态
'''
#没有点击操作之前，判断选项框状态
r = driver.find_element_by_id("boy").is_selected()
print(r)
driver.find_element_by_id("boy").click()
#点击之后判断选项框状态
l = driver.find_element_by_id("boy").is_selected()
print(l)
