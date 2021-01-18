import re
import time
import jsonpath
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_status():
    try:
        data = {
            'version': 'cloudmusic',
        }  # Get license data
        url = "https://www.nooob.top/music/others/cloudmusic.php"  # Get license url
        resp = requests.post(url=url, data=data)  # Use post to get license
        resp_json = resp.json()  # Turn json
        # ~~JSON parsing~~
        status = jsonpath.jsonpath(resp_json, '$..status')[0]
        if status == 0:
            print('软件已被关停 联系duyun888888@qq.com获取更多信息\n将在 5s 后自动退出软件')
            time.sleep(5)
            exit()
    except:
        print('NetWork ERROR, exit in 5s')
        time.sleep(5)
        exit()


get_status()
input_ = input('请输入要下载的歌曲：')
music_list = []
music_url = []
music_id = []
pattern = re.compile(r'=(.*)')
url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(input_)
print('正在加载中。。请稍等')
headers = {  # 伪造浏览器头部，不然获取不到网易云音乐的页面源代码。
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Referer': 'http://119.28.140.189/',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1'
}



options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver', options=options)
driver.get(url)
iframe_elemnt = driver.find_element_by_id("g_iframe")  # 因为直接获取不到iframe的内容，因此使用web_driver
driver.switch_to.frame(iframe_elemnt)  # 关键步骤，跳转到iframe里面，就可以获取HTML内容
# print(driver.page_source)
soup = BeautifulSoup(driver.page_source, "html.parser")  # 通过 BeautifulSoup 模块解析网页，具体请参考官方文档。
for div in soup.find_all('div',class_="ztag j-flag"):
    for title in div.find_all('div', class_='td w0'): # title
        music_list.append(title.text)
        # music_url.append(title.href)
        for a in title.find_all('a'):
            music_url.append('https://music.163.com/'+a['href'])
            # print(a, a['href'])

for id_ in music_url:
    result = pattern.findall(id_)
    music_id.append(result[0])

song_down_link = "http://music.163.com/song/media/outer/url?id=" + music_id[0] + ".mp3"  # 根据歌曲的 ID 号拼接出下载的链接。歌曲直链获取的方法参考文前的注释部分。
print("歌曲正在下载...")
response = requests.get(song_down_link, headers=headers).content  # 亲测必须要加 headers 信息，不然获取不了。
f = open(music_list[0] + ".mp3", 'wb')  # 以二进制的形式写入文件中
f.write(response)
f.close()
print("下载完成.\n\r")
print('将在 5s 后自动退出软件')
time.sleep(5)
exit()