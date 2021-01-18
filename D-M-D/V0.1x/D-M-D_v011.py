#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Copyright 2020 DY https://blog.dy6688.top
#  duyun888888@qq.com


import os
from tkinter import *
from tkinter.messagebox import *
from urllib.request import urlretrieve

import jsonpath
import requests

label_message = ''
wh_exit = ''
messages = ''

def song_download(url, title):
    os.makedirs('D-M-Downloads', exist_ok=True)
    path = 'D-M-Downloads\{}.mp3'.format(title)
    text.insert(END, '歌曲 {} 正在下载..'.format(title))
    text.see(END)
    text.update()
    urlretrieve(url, path)
    text.insert(END, '歌曲 {} 下载完毕！'.format(title))
    text.see(END)
    text.update()


def search_music_name():
  try:
    global wh_exit
    if wh_exit == 1:
      text.insert(END, messages)
      text.see(END)
      text.update()
    
    music_name = entry.get()
    plat = var.get()

    if music_name and plat:
      headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.16 Safari/537.36",
        'x-requested-with': 'XMLHttpRequest'
      }

      music_data = {
        'input': music_name,
        'filter': 'name',
        'type': plat,
        'page': 1
      }
      music_url = 'https://music.liuzhijin.cn/'
      get_search = requests.post(url=music_url, data=music_data, headers=headers)
      get_search_json = get_search.json()
      print(get_search.text)

      title = jsonpath.jsonpath(get_search_json, '$..title')[0]
      author = jsonpath.jsonpath(get_search_json, '$..author')[0]
      url = jsonpath.jsonpath(get_search_json, '$..url')[0]

      song_download(url, title)
    else:
      text.insert(END, '请检查输入内容以及下载途径 请勿为空')
      text.see(END)
      text.update()
  except:
    text.insert(END, '出现错误，请检查输入是否正确或者网络正常')
    text.see(END)
    text.update()
    text.insert(END, '如果检查后还未解决 请附上截图联系admin@dy6688.top')
    text.see(END)
    text.update()


def paste(event=None):
    entry.event_generate('<<Paste>>')


def about_developer():
    about_dev = Tk()
    about_dev.title("D-M-D's developer list")
    about_dev.geometry('200x150')
    about_label = Label(about_dev,
                        text='Developer List\nDY  duyun888888@qq.com\nhttps://blog.dy6688.top\n\nSpecial Thanks: python.org')
    about_label.grid(row=1, column=1)
    about_dev.mainloop()


root = Tk()
root.title('D-Music-download v0.11')
root.geometry('480x400+300+200')

label = Label(root, text='输入下载歌曲：', font=('楷书', 15))
label.grid(row=0, column=0)

entry = Entry(root, font=('楷书', 15))
entry.grid(row=0, column=1)

var = StringVar()
r1 = Radiobutton(root, text='酷狗', variable=var, value='kugou', )
r1.grid(row=1, column=0)
r2 = Radiobutton(root, text='QQ', variable=var, value='qq', )
r2.grid(row=1, column=1)
r3 = Radiobutton(root, text='酷我', variable=var, value='kuwo', )
r3.grid(row=2, column=0)
r4 = Radiobutton(root, text='虾米', variable=var, value='xiami', )
r4.grid(row=2, column=1)
r5 = Radiobutton(root, text='咪咕', variable=var, value='migu', )
r5.grid(row=3, column=0)
r6 = Radiobutton(root, text='百度', variable=var, value='baidu', )
r6.grid(row=3, column=1)
var.set(0)

text = Listbox(root, font=('楷书', 10), width=60, heigh=15)
text.grid(row=4, columnspan=4)

paste_button = Button(root, text='粘贴', font=('楷书', 15), command=paste)
paste_button.grid(row=0, column=3)
download_button = Button(root, text='开始下载', font=('楷书', 15), command=search_music_name)
download_button.grid(row=1, column=3)
about_button = Button(root, text='关于开发', font=('楷书', 15), command=about_developer)
about_button.grid(row=2, column=3)
exit_button = Button(root, text='双击退出', font=('楷书', 15), command=root.quit)
exit_button.grid(row=3, column=3)

footer_label = Label(root, text='Copyright 2020 DY https://blog.dy6688.top')
footer_label.grid(row=5, columnspan=4)


def get_status(): # 到网站获取使用数据
    data = {
        'from': 'D-M-D-v0.11',
    }
    url = "https://dy6688.top/music/v011.php"

    resp = requests.post(url=url, data=data)
    resp_json = resp.json()
    # 解析数据
    status = jsonpath.jsonpath(resp_json, '$..status')[0]
    message = jsonpath.jsonpath(resp_json, '$..message')[0]
    title = jsonpath.jsonpath(resp_json, '$..title')[0]
    footer_label_get = jsonpath.jsonpath(resp_json, '$..footlabel')[0]
    exit_ = jsonpath.jsonpath(resp_json, '$..exit')[0]
    global label_message
    global wh_exit
    global messages
    messages = message
    wh_exit = exit_
    label_message = footer_label_get
    if status == 0:
      showwarning(title=title, message=message)
      if exit_ == 0:
        exit()
      else:
        pass

get_status()

footer_label2 = Label(root, text=label_message)
print(label_message)
footer_label2.grid(row=6, columnspan=4)

root.mainloop()

#  Copyright 2020 DY https://blog.dy6688.top
#  duyun888888@qq.com