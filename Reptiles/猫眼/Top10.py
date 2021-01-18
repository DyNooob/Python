#  Copyright (c) 2021.  Goodboy-dy(Nooob)  https://blog.nooob.top/

import requests
import json
import bs4

url = 'https://maoyan.com/board'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS',
    'Referer': 'https://maoyan.com/board'
}


def getPage(url):
    response = requests.get(url=url, headers=headers)
    return response.text


def getInfo(hrml):
    soup = bs4.BeautifulSoup(html, 'lxml')
    items = soup.select('dd')
    for item in items:
        index = item.find('i', class_='board-index').get_text()
        name = item.find('p', class_='name').get_text()
        star = item.find('p', class_='star').get_text().strip()[3:]
        time = item.find('p', class_='releasetime').get_text()[5:]
        score = item.find('p', class_='score').get_text()

        yield {
            'index': index,
            'name': name,
            'star': star,
            'time': time,
            'score': score
        }


def writeData(file):
    with open('movie_top.txt', 'a', encoding='utf-8') as write:
        write.write(json.dumps(file, ensure_ascii=False) + '\n')



html = getPage(url)
for item in getInfo(html):
    print(item)
    writeData(item)
