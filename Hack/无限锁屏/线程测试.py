import threading
import time

cont = 0

def test(a):
    global cont
    while True:
        print(cont)
        print(a)
        if cont == 10:
            break
        time.sleep(5)

def run():
    global cont
    while True:
        cont += 1
        if cont == 1:
            test_start = threading.Thread(target=test, args=("test_data",))
            test_start.start()
        time.sleep(2)
        print(cont)


run()