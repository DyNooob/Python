#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Copyright 2020 DY https://blog.nooob.top
#  duyun888888@qq.com

"""
To do:
-- Use license x
-- Add loin    x
-- Error echo  half done
"""

# --- Import ---
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import *
from urllib.request import urlretrieve
import jsonpath
import requests

# --- Global variable ---
v = 'D-M-D-v0.21'
label_message = ''
wh_exit = ''
messages = ''
show_message = ''
show_message_time = 0
music_list = []
cont = 0
each_time = 0
show_information_time = 0


# --- Functions ---

# === Download ===
def song_download(url, title):
    os.makedirs('D-M-Downloads', exist_ok=True)
    path = 'D-M-Downloads\{}.mp3'.format(title)
    text.insert(tk.END, '歌曲 {} 正在下载..'.format(title))
    text.see(tk.END)
    text.update()
    urlretrieve(url, path)
    text.insert(tk.END, '歌曲 {} 下载完毕！'.format(title))
    text.see(tk.END)
    text.update()


# === Search music ===
def search_music_name():
    try:
        global show_message
        global show_message_time
        print(show_message)
        if show_message[0] == 0:
            if show_message_time == 0:
                text.insert(tk.END, messages)
                text.see(tk.END)
                text.update()
                show_message_time += 1

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
            text.insert(tk.END, '请检查输入内容以及下载途径 请勿为空')
            text.see(tk.END)
            text.update()
    except:
        text.insert(tk.END, '出现错误，检查输入或网络。如果检查后还未解决 请附上截图联系admin@nooob.top')
        text.see(tk.END)
        text.update()


# === Choose File Search ===
def search_file_music_name(music_list, cont):
    try:
        global show_message
        global show_message_time
        global each_time
        global show_information_time
        if show_message[0] == 0:
            if show_message_time == 0:
                text.insert(tk.END, messages)
                text.see(tk.END)
                text.update()
                show_message_time += 1
        plat = var.get()
        for each_name in range(0, cont):
            if show_information_time == 0:
                text.insert(tk.END, '批量下载开始！')
                text.see(tk.END)
                text.update()
                show_information_time += 1
            music_name = music_list[each_time]
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
                print('here')
                print(get_search.text)

                title = jsonpath.jsonpath(get_search_json, '$..title')[0]
                author = jsonpath.jsonpath(get_search_json, '$..author')[0]
                url = jsonpath.jsonpath(get_search_json, '$..url')[0]

                song_download(url, title)
                each_time += 1
            else:
                text.insert(tk.END, '请检查输入内容以及下载途径 请勿为空')
                text.see(tk.END)
                text.update()
    except:
        text.insert(tk.END, '出现错误，检查输入或网络。如果检查后还未解决 请附上截图联系admin@nooob.top')
        text.see(tk.END)
        text.update()


# === Paste button function ===
def paste(event=None):
    entry.event_generate('<<Paste>>')


# === About windows ===
def about_developer():
    about_dev = tk.Tk()
    about_dev.title("D-M-D's developer list")
    about_dev.geometry('200x150')
    about_label = tk.Label(about_dev,
                           text='Developer List\nNooob  duyun888888@qq.com\nhttps://blog.nooob.top\n\nSpecial Thanks: '
                                'python.org')
    about_label.grid(row=1, column=1)
    about_dev.mainloop()


# === Obtain License ===

def get_status():  # 到网站获取使用数据
    data = {
        'version': v,
    }  # Get license data
    url = "https://www.nooob.top/music/v0.2x/v02x.php"  # Get license url
    resp = requests.post(url=url, data=data)  # Use post to get license
    resp_json = resp.json()  # Turn json
    print(resp_json)
    # ~~JSON parsing~~
    status = jsonpath.jsonpath(resp_json, '$..status')[0]
    title = jsonpath.jsonpath(resp_json, '$..title')[0]
    message = jsonpath.jsonpath(resp_json, '$..message')[0]
    exit_ = jsonpath.jsonpath(resp_json, '$..exit')[0]
    footer_label_get = jsonpath.jsonpath(resp_json, '$..footlabel')[0]
    showmessage = jsonpath.jsonpath(resp_json, '$..show_message')
    # ~~ Global value ~~
    global label_message
    global messages
    global show_message
    show_message = showmessage
    messages = message
    label_message = footer_label_get
    # ~~ Pop-up warning ~~
    if status == 0:
        showwarning(title=title, message=message)
        if exit_ == 0:
            exit()
        else:
            pass


# === Choose download file ===
def choose_file():
    global cont
    choose = tk.Tk()
    choose.withdraw()
    Filepath = filedialog.askopenfilename()  # 获得选择好的文件
    for line in open(Filepath, encoding='utf-8'):
        if line == '\n':
            pass
        else:
            music_list.append(line.replace('\n', '').replace('\r', ''))
            print(music_list)
            cont += 1
    search_file_music_name(music_list, cont)


# --- Windows ---

root = tk.Tk()
root.title(v)
root.geometry('480x400+300+200')

# ==================

# 创建一个顶级菜单
menubar = tk.Menu(root)

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="打开文件(批量下载beta)", command=choose_file)
filemenu.add_separator()
filemenu.add_command(label="关于开发", command=about_developer)
menubar.add_cascade(label="首选项", menu=filemenu)

menubar.add_command(label="双击退出", command=root.quit)

# 显示菜单
root.config(menu=menubar)

# ====================


label = tk.Label(root, text='输入下载歌曲：', font=('楷书', 15))
label.grid(row=0, column=0)

entry = tk.Entry(root, font=('楷书', 15))
entry.grid(row=0, column=1)

var = tk.StringVar()
r1 = tk.Radiobutton(root, text='酷狗', variable=var, value='kugou', )
r1.grid(row=1, column=0)
r2 = tk.Radiobutton(root, text='QQ', variable=var, value='qq', )
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='酷我', variable=var, value='kuwo', )
r3.grid(row=2, column=0)
r4 = tk.Radiobutton(root, text='虾米', variable=var, value='xiami', )
r4.grid(row=2, column=1)
r5 = tk.Radiobutton(root, text='喜马拉雅', variable=var, value='ximalaya', )
r5.grid(row=3, column=0)
r6 = tk.Radiobutton(root, text='咪咕 接口关闭', variable=var, value='migu', state='disabled')
r6.grid(row=3, column=1)
var.set(0)

text = tk.Listbox(root, font=('楷书', 10), width=60, heigh=15)
text.grid(row=4, columnspan=4)

paste_button = tk.Button(root, text='粘贴', font=('楷书', 15), command=paste)
paste_button.grid(row=0, column=3)
download_button = tk.Button(root, text='开始下载', font=('楷书', 15), command=search_music_name)
download_button.grid(row=1, column=3)
# about_button = tk.Button(root, text='关于开发', font=('楷书', 15), command=about_developer)
# about_button.grid(row=2, column=3)
# exit_button = tk.Button(root, text='双击退出', font=('楷书', 15), command=root.quit)
# exit_button.grid(row=3, column=3)

footer_label = tk.Label(root, text='Copyright 2020 DY https://blog.nooob.top')
footer_label.grid(row=5, columnspan=4)

get_status()

footer_label2 = tk.Label(root, text=label_message)
footer_label2.grid(row=6, columnspan=4)

root.mainloop()

#  Copyright 2020 DY https://blog.nooob.top
#  duyun888888@qq.com
