from selenium import webdriver
import time

#登录
def login(driver,user,password):
    '''打开github'''
    driver.get("https://github.com/login")
    driver.implicitly_wait(10)
    #输入账号
    driver.find_element_by_id("login_field").send_keys(user)
    #输入密码
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()

def logout(driver):
    '''退出github'''
    time.sleep(3)
    driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
    time.sleep(1)
    #点击 sign out
    driver.find_element_by_css_selector(".dropdown-item.dropdown-signout").click()
    driver.quit()

if __name__== "__main__":
    driver = webdriver.Firefox()
    #调用登录
    login(driver, "Zuimengxixia", "Zuimengxixia123.")
    print("Hello yoyo!")
    #调用退出
    logout(driver)