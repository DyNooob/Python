import requests
from tqdm import tqdm

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
        print("downloading :", url_list[num])
        data = requests.get(url_list[num], headers=headers)
        with open("E:\\Python\\Reptiles\\Movies\\Movie_download\\{}.mp4".format(name[num]), "wb") as f:
            print("here")
            # f.write(data.content)
            for chunk in tqdm(data.iter_content(chunk_size=1024 * 1024)):
                if chunk:
                    f.write(chunk)
        num += 1


if __name__ == '__main__':
    url_list = ['https://vip.okokbo.com/share/yCE3MI4agnbAVuuK']
    name_list = ['生化危机']
    download(name_list, url_list)
