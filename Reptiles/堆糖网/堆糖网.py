import requests
import jsonpath
import json
import urllib.parse  # 转换类似 %E7%8B%97%E7%8B%97 的字符
from tqdm import tqdm
# 日系



def download(photos):
    num = 0
    for photo_url in tqdm(photos):
        data = requests.get(photo_url)
        with open("E:\Python\Reptiles\堆糖网\saves\{}.jpg".format(num), "wb") as f:
            f.write(data.content)
        num += 1


def request(kw):
    number = 0
    photo_list = []
    for p in tqdm(range(20)):
        url = "https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}".format(kw, number)
        resp = requests.get(url)
        web_data = resp.text
        html = json.loads(web_data)
        photos = jsonpath.jsonpath(html, "$..path")
        for w in photos:
            photo_list.append(w)
        number += 1
    print(photo_list)
    download(photo_list)


if __name__ == '__main__':
    kw = input("输入要下载的图片风格/类型：")
    kw = urllib.parse.quote(kw)
    request(kw)