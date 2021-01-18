from selenium import webdriver
from time import sleep #时间类
from selenium.webdriver.common.action_chains import ActionChains #需要引入ActionChains类,里面有鼠标调用的方法
driver=webdriver.Chrome() #打开chrome浏览器
driver.get('https://www.baidu.com/') #打开百度地址
driver.maximize_window() #窗口最大化
sleep(3)

driver.find_element_by_css_selector('#kw').send_keys('python') #定位到搜索框按钮,并输入python

#获取搜索框元素对象
element=driver.find_element_by_css_selector('#kw') #存储到变量里面,定位到搜索框
sleep(3)

#双击操作
ActionChains(driver).double_click(element).perform() # 在搜索框按钮里面双击,perform执行操作.
sleep(2)

#右击操作
ActionChains(driver).context_click(element).perform() #在搜索框按钮里面右击,perform执行操作.
sleep(2)


#鼠标悬停
above=driver.find_element_by_name("tj_settingicon") #通过name找到设置按钮
ActionChains(driver).move_to_element(above).perform() #move_to_element移到设置的元素,avove上面定位到的设置.然后执行操作
sleep(4)

driver.quit()#退出浏览器