import time
from urllib import request
import requests
import jsonpath
import json
import urllib.parse  # 转换类似 %E7%8B%97%E7%8B%97 的字符
from tqdm import tqdm


# 日系


def download(photos):
    num = 0
    cont = 0
    cont1 = 0
    for photo_url in tqdm(photos):
        if cont == 3 or cont1 == 10:
            time.sleep(0.5)
        # data = requests.get(photo_url)
        # with open("E:\Python\Reptiles\堆糖网\saves\{}.jpg".format(num), "wb") as f:
        #     f.write(data.content)
        cont += 1
        cont1 += 1
        path = "E:\Python\Reptiles\堆糖网\saves\{}.jpg".format(num)
        request.urlretrieve(photo_url, path)
        num += 1


def request_photo(kw):
    number = 1
    photo_list = []
    for p in tqdm(range(20)):
        url = "https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}".format(kw, number)
        resp = requests.get(url)
        web_data = resp.text
        html = json.loads(web_data)
        photos = jsonpath.jsonpath(html, "$..path")
        whether_done = jsonpath.jsonpath(html, "$..next_start")
        status = jsonpath.jsonpath(html, "$..status")
        message = jsonpath.jsonpath(html, "$..message")
        if status[0] != 1:
            print("出现问题啦，错误代码：", status[0])
            print(message[0])
            exit()
        print(whether_done)
        if whether_done[0] == 0:
            print("已经爬完链接")
            download(photo_list)
        for w in photos:
            photo_list.append(w)
        number = number*24
    print(photo_list)
    download(photo_list)


if __name__ == '__main__':
    kw = input("输入要下载的图片风格/类型：")
    kw = urllib.parse.quote(kw)
    request_photo(kw)
