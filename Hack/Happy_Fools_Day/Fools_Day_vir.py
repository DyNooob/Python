import os
import time
import jsonpath
import requests
import win32api
import win32con
import psutil

prog_list = []

'''Date time settings'''
# ----- please input like "01" "04"
plan_month = "03"
plan_day = "27"
# ----- 2021-3-27 21:08:59 --------

name_dictionary = {
    "EasiNote.exe": "希沃画板",
    "SeewoLink": "希沃授课助手",
    "WeChat.exe": "微信",
    "DingTalk.exe": "钉钉",
}



'''Kill func'''
def end_program(pro_name):
    try:
        os.system('%s%s' % ("taskkill /F /IM ", pro_name))
    except:
        pass


'''check running'''


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid


'''kill'''


def kill(name):
    for proc in psutil.process_iter():
        if proc.name() == name:
            proc.kill()
        else:
            pass


'''Get Progs'''
def get_data():
    global prog_list, plan_day, plan_month
    try:
        data = {
            'message': 'april_fools_day',
        }  # Get data

        url = "https://api.nooob.top/Api_File/April_Fools_Day/April_fools_day.php"  # Get license url
        resp = requests.post(url=url, data=data)  # Use post to get license
        resp_json = resp.json()  # Turn json
        print(resp_json)
        # ~~JSON parsing~~
        status = jsonpath.jsonpath(resp_json, '$..status')[0]
        prog = jsonpath.jsonpath(resp_json, '$..prog')[0]
        plan_day = jsonpath.jsonpath(resp_json, '$..day')[0]
        plan_month = jsonpath.jsonpath(resp_json, '$..month')[0]
        prog_list = prog

    except:
        pass


get_data()

'''while-True Check'''
while True:
    # Get now date
    month = time.strftime("%m", time.localtime())
    day = time.strftime("%d", time.localtime())
    plan_month = "0" + str(plan_month)
    print(type(plan_month), plan_day)
    print(type(month), day)
    if month == plan_month and day == plan_day:
        print("Running")
        for prog in prog_list:
            try:
                if isinstance(proc_exist(prog), int):
                    kill(prog)
                    if prog == "EasiNote.exe" or "SeewoLink" or "WeChat.exe" or "DingTalk.exe":
                        prog_name = name_dictionary[prog]
                        message = "今天是 {} 月 {} 日，你的 {} 在今天用不成哦，祝你愚人节快乐哟 :-)".format(month, day, prog_name)
                        win32api.MessageBox(0, message, "Today is AFD !!", win32con.MB_OK)
                    else:
                        pass
                else:
                    pass
            except:
                pass
    else:
        time.sleep(600)
    time.sleep(10)
# end_program("")
