#  Copyright (c) 2021.  Goodboy-dy(Nooob)  https://blog.nooob.top/
import win32con  # 定义
import win32gui  # 界面
import time  # 时间
import lock_gui
import threading
import keyboard
import psutil  # 检测进程


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid


def check():
    while True:
        if isinstance(proc_exist('V1.0.exe'), int):
            print('V1.0.exe正在运行')
        else:
            pass


def keyb():
    while True:
        try:
            if keyboard.is_pressed('ctrl+shift+s'):
                print('1')
                show()
            elif keyboard.is_pressed('ctrl+shift+h'):
                print('2')
                hide()
            else:
                pass
        except Exception as e:
            error_time = time.asctime(time.localtime(time.time()))
            with open('error0000.txt', 'a', encoding='utf-8') as write:
                write.write('-' * 10 + '\n')
                write.write(error_time + '\n')
                write.write('错误类型是' + e.__class__.__name__ + '\n')
                write.write('错误明细是' + e + '\n')
            break


def password_lock():
    lock_gui.up()


def check_pwd_torf():
    if lock_gui




def show():
    try:
        Application_lock = win32gui.FindWindow("TkTopLevel", "Application_lock")
        if Application_lock:
            win32gui.ShowWindow(Application_lock, win32con.SW_SHOW)  # 设置显示
        else:
            pass
    except Exception as error:
        error_time = time.asctime(time.localtime(time.time()))
        with open('error0000.txt', 'a', encoding='utf-8') as write:
            write.write('-' * 10 + '\n')
            write.write(error_time + '\n')
            write.write('错误类型是' + error.__class__.__name__ + '\n')
            write.write('错误明细是' + error + '\n')


def hide():
    try:
        Application_lock = win32gui.FindWindow("TkTopLevel", "Application_lock")
        if Application_lock:
            win32gui.ShowWindow(Application_lock, win32con.SW_HIDE)  # 设置隐藏
        else:
            pass
    except Exception as error:
        error_time = time.asctime(time.localtime(time.time()))
        with open('error0000.txt', 'a', encoding='utf-8') as write:
            write.write('-' * 10 + '\n')
            write.write(error_time + '\n')
            write.write('错误类型是' + error.__class__.__name__ + '\n')
            write.write('错误明细是' + error + '\n')


def main():
    passwd_lock = threading.Thread(target=password_lock)
    key = threading.Thread(target=keyb)

    passwd_lock.start()
    key.start()


if __name__ == "__main__":
    main()
