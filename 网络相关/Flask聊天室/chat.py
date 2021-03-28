from flask import Flask,request,render_template
import json
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

user_dict = {}

chat_app = Flask(__name__)
@chat_app.route('/ws/<username>')
def ws_chat(username):
    user_socket = request.environ.get('wsgi.websocket') # type:WebSocket
    user_dict[username]=user_socket
    while 1:
        msg = user_socket.receive()  # 等待接收客户端发来的数据
        msg_dict = json.loads(msg)
        msg_dict['from_user'] = username
        to_user = msg_dict.get('to_user')
        if to_user == "":  # 如果用户名是空表示群发
            for uname, uwebsocket in user_dict.items():
                if uname == username:  # 群发时不用给自己发
                    continue
                uwebsocket.send(json.dumps(msg_dict))
            continue
        to_user_socket = user_dict.get(to_user)
        if not to_user_socket:  # 判断用户字典中是否存在用户的websocket连接
            continue
        try:
            msg_dict['from_user'] = msg_dict['from_user'] + '@私聊我'
            to_user_socket.send(json.dumps(msg_dict))
        except:
            user_dict.pop(to_user)

@chat_app.route('/webchat')
def webchat():
    return render_template('public_chat.html')

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0',9527),chat_app,handler_class=WebSocketHandler)
    server.serve_forever()