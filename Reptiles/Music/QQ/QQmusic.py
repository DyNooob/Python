#  Copyright (c) 2021.  Goodboy-dy(Nooob)  https://blog.nooob.top/
# https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E6%9B%BE%E4%BB%8A%E7%9A%84%E4%BD%A0
import urllib.parse as parse
from urllib.request import urlretrieve

import jsonpath
import requests
import json
import os
import time
import sys

print('Copyright (c) 2021.  Goodboy-dy(Nooob)  https://blog.nooob.top/')

def get_status():
    try:
        data = {
            'version': 'qqmusic',
        }  # Get license data
        url = "https://www.nooob.top/music/others/qqmusic.php"  # Get license url
        resp = requests.post(url=url, data=data)  # Use post to get license
        resp_json = resp.json()  # Turn json
        # ~~JSON parsing~~
        status = jsonpath.jsonpath(resp_json, '$..status')[0]
        if status == 0:
            print('软件已被关停 联系duyun888888@qq.com获取更多信息\n将在 5s 后自动退出软件')
            time.sleep(5)
            exit()
        else:
            print('软件已获得作者授权\n仅供学习使用 使用此软件所带来的一切责任由使用者承担')
    except:
        print('NetWork ERROR, exit in 5s')
        time.sleep(5)
        exit()


get_status()


def Time_1():  # 进度条函数
    for i in range(1, 51):
        sys.stdout.write('\r')
        sys.stdout.write('进度： {0}% |{1}'.format(int(i % 51) * 2, int(i % 51) * '■'))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')


w = parse.urlencode({'w': input('歌曲名称:')})

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63229658163010696&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&%s&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0' % (
    w)

content = requests.get(url=url)

str_1 = content.text

dict_1 = json.loads(str_1)

song_list = dict_1['data']['song']['list']

str_3 = '''https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"1825194589","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'''

url_list = []
music_name = []

print('序号 -- 歌曲名 -- 歌手')

for i in range(len(song_list)):
    music_name.append(song_list[i]['name'] + '-' + song_list[i]['singer'][0]['name'])
    print('{}. {} -- {}'.format(i + 1, song_list[i]['name'], song_list[i]['singer'][0]['name']))
    url_list.append(str_3 % (song_list[i]['mid']))

id = int(input('请输入你想下载的音乐的序号:'))

content_json = requests.get(url=url_list[id - 1])

dict_2 = json.loads(content_json.text)

url_ip = dict_2['req']['data']['freeflowsip'][1]

purl = dict_2['req_0']['data']['midurlinfo'][0]['purl']

downlad = url_ip + purl

try:
    os.mkdir('./QQmusic')
except:
    pass

finally:
    try:
        print('正在下载中...')
        urlretrieve(url=downlad, filename='./QQmusic/{}.mp3'.format(music_name[id - 1]))
        Time_1()
        print('歌曲 {} 下载完成！'.format(music_name[id - 1]))
        print('将在 5s 后自动退出软件')
        time.sleep(5)
        exit()
    except Exception as e:
        print('出现错误： ', e)
        print('将在 5s 后自动退出软件')
        time.sleep(5)
        exit()
