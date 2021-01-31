import urllib.request
import urllib.parse
# import json
from bs4 import BeautifulSoup

search_word = input("请输入你要搜的电影: ")

index_url = "https://okzyw.com"

headers = {
    "referer": "https://okzyw.com/index.php?m=vod-search",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 FS",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "UM_distinctid=1775184580d9-065b76713d419c-4c3f217f-1fa400-1775184580e1f5; CNZZDATA1263424981=1230232964-1611978421-%7C1611978421; PHPSESSID=ijvu19t11eph29d598qq3eonj3"
}

url = "https://okzyw.com/index.php?m=vod-search"
# url = "http://httpbin.org/post"
search_data = {
    "wd": search_word,
}

postdata = urllib.parse.urlencode(search_data).encode('utf-8')
req = urllib.request.Request(url=url, headers=headers, data=postdata, method='POST')
response = urllib.request.urlopen(req)
# html = response.read()
html_data = response.read().decode('utf-8')
# print(html_data)
soup = BeautifulSoup(html_data, 'html.parser')
for span in soup.find_all('span', class_="xing_vb4"):
    # print(span.text)
    for a in span.find_all("a"):
        print(a.text, index_url + a["href"])