# #!/usr/bin/env python
# #-*- coding:utf-8 -*-

# # 注册模块

# import os
# from urllib.request import urlretrieve
# import requests
# import jsonpath
# from bs4 import BeautifulSoup



# data = {
# 	'license': 'mm',
# }

# url = 'https://dy6688.top/music/license.php'

# resp = requests.post(url=url, data=data)
# resp_json = resp.json()
# # 解析数据
# status = jsonpath.jsonpath(resp_json, '$..status')[0]
# # status判断是否错误(0为错误，1为正确)
# if status == 0:
# 	print('激活码错误')
# elif status != 0 or status != 1:
# 	print('错误码 %s，'%status)
# else:
# 	expire = jsonpath.jsonpath(resp_json, '$..expire')[0]# 是否到期
# 	dutime = jsonpath.jsonpath(resp_json, '$..dutime')[0]# 到期时间
# 	if expire == 'yes':
# 		print('到期')
# 	elif expire == 'no':
# 		print('未到期, 到期时间 --', dutime)
import datetime
ti = datetime.datetime.strptime("2006-01-26 07:08", '%Y-%m-%d %H:%M')
t2 =  datetime.datetime.strptime("2021-02-07 11:33", '%Y-%m-%d %H:%M')
t3 = t2 - ti
print(t3)