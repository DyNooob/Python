import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS',
    "Cookie": "FSSBBIl1UgzbN7N80S=r12Oaj3cU..UTCl7.pReN7J5gQ11Qxjpj7F.4z70OsKN.WX1acm907fFNS.xFWC5; FSSBBIl1UgzbN7N80T=46NgmVjcXnFF8AMC3XJNKlpQBI8Iz576dZWjeKqgH.QQvBQpZwLxM9CePVdp9YaGgBz7RZO8q8vMKLjh58UkZzMDBSI3eyFLD2sa5xWPO6YsW9vnZvIZAHaY2m2YxQm82_9MOpAf9Q8UwPyyA6SEzxhdJI2h7aOSkU.aYDxiQ8hUPddo.MmZAuKcpEcyDbW33Nw_nf7iqOapLfYDpUvyK26ybTTX7EFw42YTZrMwyF5dJV.Q_ptFjGIW9oPX_WB8guTRjs187dsaGtsuKH6f4i.PMfmgvzb_UlyoHSQYe0WLi_fqfM2XEhpEVSPQmHKYuZqJ.gXA2.JYCh3ZK9w7Zozw7",
    "Host": "www.xiantao.gov.cn",
    "Referer": "http://www.xiantao.gov.cn/hdjl/lygk/"
}

proxy = {
    'http': 'http://' + "58.220.95.86:9401"
}

url = "http://www.xiantao.gov.cn/hdjl/lygk/"

# p = requests.get(url=url, headers=headers, proxies=proxy)#  timeout=3

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver', options=options)
driver.get(url)
iframe_elemnt = driver.find_element_by_id("g_iframe")  # 因为直接获取不到iframe的内容，因此使用web_driver
driver.switch_to.frame(iframe_elemnt)  # 关键步骤，跳转到iframe里面，就可以获取HTML内容
# print(driver.page_source)