import pickle
from io import BytesIO
import socket

def server_pic(ip, port):
    socket_obj = socket.socket(socket.AF_INET)
