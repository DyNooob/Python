import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

'''
TODO:
注册淘宝账号重启此程序编写
淘宝设定不登录不能搜索啊。。。
'''

'''
2021-1-27 22:17:55 DY(Nooob)
    - 所有time.sleep都是用来等待响应的，根据网速调整sleep时间
    - click: 点击(所点击的要是一个按钮)
    - xpath说明: 用Chrome的元素查找可以定位元素位置，右键"Copy"=>"Copy xpath"可以复制到元素xpath路径
'''


class Taobao_Infos:
    def __init__(self):
        url = "https://login.taobao.com/member/login.jhtml"
        self.url = url
        self.browser = webdriver.Chrome(executable_path="C:\\Python\\things\\browsers\\chromedriver.exe")
        self.wait = WebDriverWait(self.browser, 10)

    def login_info(self):
        self.browser.get(self.url)
        if self.browser.find_element_by_xpath('//*[@id="login"]/div[1]/i'):
            self.browser.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
        time.sleep(5)

        taobao_index_page = self.browser.find_element_by_xpath("//*[@id='J_SiteNavHome']/div/a")
        taobao_index_page.click()
        time.sleep(1)

        search_input = self.browser.find_element_by_xpath('//*[@id="q"]')
        search_name = input("输入您要搜索的内容：")
        search_input.send_keys(search_name)
        time.sleep(0.5)

        search_submit = self.browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
        search_submit.click()
        time.sleep(0.5)

        page = self.browser.page_source
        # page 为网页源码

        soup = BeautifulSoup(page, 'lxml')
        goods_data_list = soup.find('div', class_='')
        # 写不了了，没账号，不能登录。。。


taobao = Taobao_Infos()
taobao.login_info()
