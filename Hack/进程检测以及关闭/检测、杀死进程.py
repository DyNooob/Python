import psutil
import time
import os
from os import system
import threading
import tkinter
import tkinter.messagebox




def choose_time_out():
    time.sleep(15)
    os.system('taskkill /f /im %s' % 'POWERPNT.EXE')
    tkinter.messagebox.showinfo('提示', '选择超时')


choose_time = threading.Thread(target=choose_time_out, args=())


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid


def kill():
    choose_time.start()  # 选择计时
    top = tkinter.Tk()
    top.wm_attributes('-topmost',1)
    top.withdraw()
    top.update()
    a = tkinter.messagebox.askquestion('提示', '已到下课时间，点击是且在10s之内关闭PPT下课！不然。。')

    print(a)

    if a == 'yes':  # 是
        try:
            print('yes')
            time.sleep(10)  # 60秒等待关闭
            os.system('taskkill /f /im %s' % 'POWERPNT.EXE')
            tkinter.messagebox.showwarning('emm', '难道忘记了刚刚选的啥？我帮你关了哈')
            while True:
                if isinstance(proc_exist('POWERPNT.EXE'), int):
                    time.sleep(1)
                    os.system('taskkill /f /im %s' % 'POWERPNT.EXE')
                    tkinter.messagebox.showerror('提示', '记住你的选择！')
                else:
                    pass
        except:
            top.mainloop()
    # elif a == None:  # 取消
    #     tkinter.messagebox.showerror('选的好！', '一个不错的选择')
    #     time.sleep(5)
    #     # os.system("shutdown -s -t  10 ") # 直接关机
    else:  # 否
        while True:
            if isinstance(proc_exist('POWERPNT.EXE'), int):
                time.sleep(1)
                os.system('taskkill /f /im %s' % 'POWERPNT.EXE')
                tkinter.messagebox.showerror('提示', '天降正义！')
            else:
                pass


def check():
    if isinstance(proc_exist('POWERPNT.EXE'), int):
        time.sleep(10)  # test
        print('PPT正在运行')
        kill()
    else:
        print('PPT未运行')


def main():
    print('Running')
    check()


if __name__ == "__main__":
    main()
