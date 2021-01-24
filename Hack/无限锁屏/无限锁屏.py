from ctypes import *
import time

import jsonpath
import requests
import win32gui
import threading

sleep_time = 1000
status = 1


def lock(sleep_time):
    while True:
        user32 = windll.LoadLibrary("user32.dll")
        user32.LockWorkStation()
        time.sleep(sleep_time)




def get_status():  # 到网站获取使用数据
    global status, sleep_time
    while True:
        # try:
            data = {
                'version': 'Lock',
            }  # Get license data
            url = "https://api.nooob.top/Api_File/锁屏/lock.php"  # Get license url
            resp = requests.post(url=url, data=data)  # Use post to get license
            resp_json = resp.json()  # Turn json
            print(resp_json)
            # ~~JSON parsing~~
            status = jsonpath.jsonpath(resp_json, '$..status')[0]
            sleep_time = jsonpath.jsonpath(resp_json, '$..second')[0]

            if status == 0:
                lock_scr = threading.Thread(target=lock, args=(sleep_time,))
                lock_scr.start()
            else:
                pass
            time.sleep(10)
        # except:
        #     status = 1
        #     sleep_time = 0
        #     time.sleep(6000)


# while True:  # 隐藏窗口
#     try:
#         Application_lock = win32gui.FindWindow("TkTopLevel", "Application_lock")
#     except:
#         pass


if __name__ == '__main__':
    get_sta = threading.Thread(target=get_status)

    get_sta.start()
