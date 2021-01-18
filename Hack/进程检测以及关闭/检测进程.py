import psutil
import time
import os
from os import system
import threading
import tkinter
import tkinter.messagebox


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid


def check():
    if isinstance(proc_exist('SeewoLink.exe'), int):
        print('SeewoLink.exe正在运行')
    else:
        print('无')


def main():
    print('Running')
    check()


if __name__ == "__main__":
    main()





