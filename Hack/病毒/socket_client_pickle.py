import socket
from io import BytesIO
import pickle


def client_pic(ip, port, obj):
    try:
        msg = pickle.dumps(obj)
        send_message = BytesIO(msg)
        send_message_from = send_message.read(1024)
    except:
        send_message = obj
        send_message_from = send_message.read(1024)
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.connect((ip, port))

    while send_message_from:
        socket_obj.send(send_message_from)
        send_message_from = send_message.read(1024)

    socket_obj.close()

if __name__ == "__main__":
    dict_data = {'key1': 'welcome dy', 'key2': [1, 3]}

    client_pic('192.168.123.26', 6666, dict_data)