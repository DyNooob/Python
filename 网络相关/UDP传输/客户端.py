import socket
from socket import *
import threading

server_ip = '192.168.123.99'
server_port = 12355
coding = 'utf-8'
message = 'Hello World!'
user_list = ''


def send_information(ip, port, message):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    send_addr = (ip, port)
    udp_socket.sendto(message.encode(coding), send_addr)
    udp_socket.close()


def choose_user(server_ip, server_port):
    message = '>>!-get_user_list'
    send_information(server_ip, server_port, message)
    time.sleep(0.5)
###
    if user_list != '':
        return user_list
    else:
        return 'Error'

def send(ip, port, coding, message):
    message = input("Input your message: ")
    if message == ':u':
        choose_user(ip, port)
    else:
        message = message+'>-'+to_user
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    send_addr = (ip, port)
    udp_socket.sendto(message.encode(coding), send_addr)
    udp_socket.close()


def receive_status():
    global server_ip, server_port, coding, message, user_list
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 12366))
    while True:
        recvInfo = udp_socket.recvfrom(1024)
        if recvInfo[0].decode("utf-8") == '1':
            send_status = 'Success'
        elif recvInfo[0].decode("utf-8")[0:2] == '201':
            user_list = recvInfo[0].decode("utf-8")[4:]
        else:
            send_status = 'Error'
        print("发信状态 [%s]"%send_status)
        # print("收到消息：", recvInfo[0].decode("utf-8"))
        send(server_ip, server_port, coding, message)

if __name__ == '__main__':
    send_ = threading.Thread(target=send, args=(server_ip, server_port, coding, message))
    receive_ = threading.Thread(target=receive_status)

    # send_.start()
    receive_.start()