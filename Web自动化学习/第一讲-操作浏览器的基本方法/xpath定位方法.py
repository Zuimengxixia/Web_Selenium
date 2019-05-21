from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#用xpath通过ID定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")

#用xpath通过name定位
driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")

#用xpath通过class定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")

#用xpath通过其它方式定位
driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("python")

#用xpath通过ID定位 通过标签筛选
driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")

#用xpath通过name定位 通过标签筛选
driver.find_element_by_xpath("//input[@name='wd']").send_keys("python")

#用xpath通过class定位 通过标签筛选
driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")

#用xpath通过其它方式定位 通过标签筛选
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("python")

#用xpath通过定位他爷爷来定位input输入框
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python")

#用xpath通过定位老大、老二、老三（如果一个元素它的兄弟元素跟它的标签一样）按先后顺序（索引）定位
driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()

#xpath逻辑运算 运用 and（与）or（或）not（非）
driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").click()

#xpath模糊匹配功能
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()

#xpath也可以模糊匹配某个属性
driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()

#xpath可以模糊以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()

#xpath可以模糊以什么结尾
driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()

#xpath还能支持最强的正则表达式
driver.find_element_by_xpath("//*[matchs(text(),'hao13')]").click()