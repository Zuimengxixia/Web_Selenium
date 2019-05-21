from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# css 通过id属性定位
driver.find_element_by_css_selector("#kw").send_keys("python")

# css 通过class属性定位
driver.find_element_by_css_selector(".s_ipt").send_keys("python")

# css 通过标签属性定位，注意写法（在这个例子是会报错的）
driver.find_element_by_css_selector("input").send_keys("python")

# css 通过 name 属性定位
driver.find_element_by_css_selector("[name='wd'").send_keys("python")

# css 通过 autocomplete 属性定位
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python")

# css 通过 type 属性定位
driver.find_element_by_css_selector("[type='text']").send_keys("python")

# css 通过标签于calss 属性的组合定位
driver.find_element_by_css_selector("input.s_ipt").send_keys("python")

# css 通过标签于id属性的组合定位
driver.find_element_by_css_selector("input#kw").send_keys("python")

# css 通过标签于其它属性组合定位
driver.find_element_by_css_selector("input[id='kw']").send_keys("python")

# css 通过层级关系来定位 例：xpath://form[@id='form']/span/input和//form[@class='fm']/span/input
driver.find_element_by_css_selector("form#form>span>input").send_keys("python")
driver.find_element_by_css_selector("form.fm>span>input").send_keys("python")

# css 索引 通过 nth-child（）来定位
driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()

# css 逻辑运算
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")
