import requests
from bs4 import BeautifulSoup

url = 'https://www.ximalaya.com/xiangsheng/61/'
a = 2

url = url + '/p{}'.format(a)
print(url)