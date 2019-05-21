from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
ActionChains(driver).context_click(mouse).perform()
ActionChains(driver).double_click().perform()
