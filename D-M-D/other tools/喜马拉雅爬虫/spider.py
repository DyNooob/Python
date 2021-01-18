# -*- coding:utf-8 -*-
# url = 'https://www.ximalaya.com/xiangsheng/61/'

import time
import jsonpath
import requests
from bs4 import BeautifulSoup
page_cont = 1
cont = 0
page_cont_list = []


def get_status():  # 到网站获取使用数据
    try:
        data = {
            'version': 'xmly',
        }  # Get license data
        url = "https://www.nooob.top/music/others/ximalaya.php"  # Get license url
        resp = requests.post(url=url, data=data)  # Use post to get license
        resp_json = resp.json()  # Turn json
        print(resp_json)
        # ~~JSON parsing~~
        status = jsonpath.jsonpath(resp_json, '$..status')[0]
        if status == 0:
            print('项目关闭')
            time.sleep(3)
            exit()
        else:
            pass
    except:
        print('server error')


def spider(url):
    if url:
        url1 = url
        try:
            global page_cont
            global cont
            headers = {"User-Agent":
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
                       }
            html = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html, "html.parser")
            for a in soup.find_all('a', class_='page-link WJ_'):
                page_cont_list.append(a.text)
            while True:
                print(url)
                headers = {"User-Agent":
                               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
                           }
                html = requests.get(url, headers=headers).text
                soup = BeautifulSoup(html, "html.parser")
                for div in soup.find_all('div', class_="text lF_"):
                    for a in div.find_all('a'):
                        print(a.text)
                        if a.text != '':
                            with open("download_file.txt", "a", encoding='utf-8') as f:
                                f.write(a.text + '\n')
                                cont = cont+1
                        else:
                            print('一共发现 {} 首 文件已保存至 download_file.txt'.format(cont))
                            break
                if page_cont == int(page_cont_list[-2]):
                    print('一共发现 {} 首 文件已保存至 download_file.txt'.format(cont))
                    main()
                    break
                else:
                    page_cont += 1
                    url = url1 + '/p{}'.format(page_cont)

        except:
            print('Error, 请检查链接是否为喜马拉雅专辑链接！')
            main()
    else:
        print('输入不能为空 请检查后再次输入')
        main()


def main():
    url = input('输入喜马拉雅链接：')
    spider(url)

if __name__ == '__main__':
    get_status()
    main()