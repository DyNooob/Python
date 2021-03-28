import socket
from socket import *

'''
返回:
-- 201+用户列表

接受:
    >>!-get_user_list
        获取用户
    >>!-chosed+uid
        选择和uid为uid的用户聊天

格式:
    >> User list
            201{'uid':'uname', 'uid2':'uname2'}



'''

def reply(c_ip):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    send_addr = (c_ip, 12366)
    udp_socket.sendto('1'.encode("utf-8"), send_addr)
    udp_socket.close()


def receive():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 12355))
    while True:
        recvInfo = udp_socket.recvfrom(1024)
        from_message = recvInfo[0].decode("utf-8")
        if from_message.split('>>!-')[1:] == 'get_user_list':
            user_list
            # 懒得写了 暂时放一下
            # 2021-1-28 22:21:41
        print("[%s]: %s" % (str(recvInfo[1]), recvInfo[0].decode("utf-8")))
        reply(recvInfo[1][0])


def send():
    pass

receive()
