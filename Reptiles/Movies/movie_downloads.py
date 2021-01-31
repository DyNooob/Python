import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

movie_url_list = []
movie_name_list = []
num = 0

headers = {
    "referer": "https://okzyw.com/index.php?m=vod-search",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 FS",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "UM_distinctid=1775184580d9-065b76713d419c-4c3f217f-1fa400-1775184580e1f5; CNZZDATA1263424981=1230232964-1611978421-%7C1611978421; PHPSESSID=ijvu19t11eph29d598qq3eonj3"
}


def download(name, url_list):
    global num
    for d in tqdm(url_list):
        data = requests.get(url_list[num], headers=headers)
        with open("E:\\Python\\Reptiles\\Movie_download\\{}.mp4".format(name[num]), "wb") as f:
            # f.write(data.content)
            for chunk in data.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        num += 1




def get_data(url):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    for div in soup.find_all("div", id="down_1"):
        for id in div.find_all('li'):
            movie_url = "http" + id.text.split('http')[1]
            start_place = movie_url.rfind("/") + 1
            stop_place = movie_url.rfind(".mp4")
            movie_name = movie_url[start_place:stop_place]
            movie_name_list.append(movie_name)
            movie_url_list.append(movie_url)
            download(movie_name_list, movie_url_list)


if __name__ == '__main__':
    # url = input("页面地址：")
    url = "https://okzyw.com/?m=vod-detail-id-13476.html"
    get_data(url)