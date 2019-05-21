from  selenium import  webdriver
import time

url = "http://meibbcc.com/"
driver1 = webdriver.Ie()
driver2 = webdriver.Firefox()
driver3 = webdriver.Chrome()
drivers =(driver1,driver2,driver3)

for driver in drivers:
    driver.get(url)
    driver.implicitly_wait(30)

