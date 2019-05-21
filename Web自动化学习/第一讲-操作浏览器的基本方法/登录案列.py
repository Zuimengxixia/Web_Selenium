from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://github.com/login")
driver.implicitly_wait(10)

#输入账号
driver.find_element_by_id("login_field").send_keys("Zuimengxixia")

#输入密码
driver.find_element_by_id("password").send_keys("Zuimengxixia123.")

#点击登录
driver.find_element_by_name("commit").click()

# 登录成功后，获取我的账户名称
time.sleep(5)
# 点右上角设置
driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
# 获取账户名称
time.sleep(1)
t = driver.find_element_by_xpath('//*[@id="user-links"]/li[3]/details/details-menu/ul/li[1]/a/strong').text
print("获取到我的账户名称：%s" % t)

if t == "Zuimengxixia":
    print("登录成功！")
else:
    print("登录失败！")
