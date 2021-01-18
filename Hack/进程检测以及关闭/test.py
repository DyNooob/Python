import psutil


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        print(psutil.Process(pid).name())
        if psutil.Process(pid).name() == process_name:
            return pid

def check():
    if isinstance(proc_exist('python.exe'), int):
        print('Python is running')
    else:
        print('无')


check()