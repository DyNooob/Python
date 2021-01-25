from ctypes import *
import time

import jsonpath
import requests

cont = 0
sleep_time = 1000
status = 1


def lock(sleep_time):
    global cont
    while True:
        user32 = windll.LoadLibrary("user32.dll")
        user32.LockWorkStation()
        time.sleep(sleep_time)
        if cont == 4:
            cont = 0
            get_status()
            break
        else:
            pass
        cont += 1


def get_status():
    global status, sleep_time
    while True:
        try:
            data = {
                'version': 'Lock',
            }
            url = "https://api.nooob.top/Api_File/锁屏/lock.php"
            resp = requests.post(url=url, data=data)
            resp_json = resp.json()
            print(resp_json)
            status = jsonpath.jsonpath(resp_json, '$..status')[0]
            sleep_time = jsonpath.jsonpath(resp_json, '$..second')[0]

            if status == 0:
                lock(sleep_time)
            else:
                time.sleep(1000)
        except:
            time.sleep(6000)


if __name__ == '__main__':
    get_status()
