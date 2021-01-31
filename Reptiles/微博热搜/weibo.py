#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   written by DY(Nooob)
   https://blog.nooob.top/
   e-mail:duyun888888@qq.com
"""

import urllib.request
from bs4 import BeautifulSoup
import time
from openpyxl import workbook

star = '*'
newline = "\n"
separator = '-'
count_ = 0
print("Nooob's blog https: // blog.nooob.top / ")
rs = 'https://s.weibo.com/top/summary?'
side = 'https://s.weibo.com'

while True:
    page = urllib.request.urlopen(rs)
    html = page.read()
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    now = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['排名', '时间', '姓名', '链接'])
    a = BeautifulSoup(html, 'html.parser')
    print('微博实时热搜榜  时间：', now)
    print('-' * 15, '50条热搜', '-' * 15)
    for tbody in soup.find_all('tbody'):
        for a in tbody.find_all('a', target='_blank'):
            url = side + a['href']
            text_ = a.text
            count_ = count_ + 1
            ws.append([count_, now, text_, url])
            print(newline, '第', count_, "条 ", separator*20, newline)
            print(text_, '  链接：', url)
    time_ = (time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{min}", time.localtime())).format(y='年', m='月', d='日', h='时', min='分')
    print(separator * 15, '结束', separator * 15)
    filename1 = '微博热搜'
    filename2 = '.xlsx'
    filename_ = str(filename1 + time_ + filename2)
    wb.save(filename_)  # 存入所有信息后，保存为.xlsx
    print(newline, star*10, newline, '爬取文件已保存至同级目录下的', newline, filename_, '文件中……', newline, star*10)
    break
# 如果需要反复爬取，请注释'break'，并将下面这条注释去掉
# time.sleep(1800)# 等待半小时后再次爬取
