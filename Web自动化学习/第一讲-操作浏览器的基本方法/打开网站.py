from selenium import webdriver
import time

'''打开网站'''
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
'''设置浏览器窗口为540*960大小'''
driver.set_window_size(540,960)
time.sleep(3)
'''设置浏览器窗口最大化'''
driver.maximize_window()

driver.get("http://www.hordehome.com")
'''设置休眠时间'''
time.sleep(3)
'''返回上一页'''
driver.back()
time.sleep(3)
'''切换到下一页'''
driver.forward()

'''等待三秒后刷新页面'''
driver.refresh()
driver.quit()
