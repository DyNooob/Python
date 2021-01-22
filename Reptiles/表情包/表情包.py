import requests
import bs4
from tqdm import tqdm

'''
img class="ui image lazy"
'''
cont = 0
page_cont = 0
img_url_list = []
url = "https://www.fabiaoqing.com/bqb/lists/page/%s.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def img_download(img_list):
    global cont
    for img_url in tqdm(img_list):
        cont += 1
        img = requests.get(img_url, headers=headers, stream=True)
        if img_url[-3:] == "gif":
            img_last = 'jpg'
        else:
            img_last = img_url[-3:]
        with open('./saves/%s.%s' % (cont, img_last), 'wb') as w:
            for img_write in img.iter_content(chunk_size=32):
                w.write(img_write)


def get_image_url(url):
    global page_cont
    for page in tqdm(range(1, 200)):
        page_cont += 1
        page_url = url % (page_cont)
        html = requests.get(page_url, headers=headers).text
        soup = bs4.BeautifulSoup(html, "html.parser")
        for img_url in soup.find_all('img', class_="ui image lazy"):
            img_url_list.append(img_url["data-original"].replace("bmiddle", "large"))

    img_download(img_url_list)


get_image_url(url)
