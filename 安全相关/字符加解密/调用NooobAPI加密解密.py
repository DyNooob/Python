import time

import jsonpath
import requests
import getpass
import json
api = "https://api.nooob.top/Api_File/ed/ed.php"

mod = input("请输入您要进行的操作\n'1'为加密,'2'为解密：")
text = input("请输入原文/密文：")
key = getpass.getpass("请输入密匙(不会显示)：")

jiemi_data = {"version":"django-tools",
        "jiemi_word":text,
        "jiemi_key":key
}
jiami_data = {"version":"django-tools",
        "jiami_word":text,
        "jiami_key":key,
}


if int(mod) == 1:
  data = jiami_data
elif int(mod) == 2:
  data = jiemi_data
else:
  print("未知模式: ", mod)
  print("即将在5s后自动退出....")
  time.sleep(5)

if text == '':
    print("未检测到输入内容，请检查后重试")
    print("即将在5s后自动退出....")
    time.sleep(5)
if key == '':
    print("未检测到key, 使用默认密匙: Nooob")

res = requests.post(url=api,data=data)

res = json.loads(res.text)

return_text = jsonpath.jsonpath(res, "$..ed")
status = jsonpath.jsonpath(res, "$..status")
key = jsonpath.jsonpath(res, "$..key")

key = key[0]
key_len = len(key)
key_1 = key[0:3]
key_2 = "*"*(key_len-3)
key_show = key_1+key_2

return_data = return_text[0]
if return_data == '':
    return_data = "无解密内容，请检查"

print("得到的密文为：\n", "-"*20, '\n', return_data, "\n", "-"*20)
if int(mod) == 1:
  print("您的密匙为：\n", "-"*20, '\n', key_show, "\n", "-"*20)

print("即将在5s后自动退出....")
time.sleep(5)
