#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymouse import PyMouse
import time
import threading

check_time = 1000
time_sleep = 1

m = PyMouse()
time.sleep(time_sleep)
print(m.position())


def check():
    for a in range(1, check_time):
        m.click(894, 825, 1)
        time.sleep(0.00001)
        if a == check_time:
            break


check1 = threading.Thread(target=check)
check1.start()
check2 = threading.Thread(target=check)
check2.start()
check3 = threading.Thread(target=check)
check3.start()
check4 = threading.Thread(target=check)
check4.start()
check5 = threading.Thread(target=check)
check5.start()
check6 = threading.Thread(target=check)
check6.start()
check7 = threading.Thread(target=check)
check7.start()
check8 = threading.Thread(target=check)
check8.start()
check9 = threading.Thread(target=check)
check9.start()
check10 = threading.Thread(target=check)
check10.start()
check11 = threading.Thread(target=check)
check11.start()
check12 = threading.Thread(target=check)
check12.start()
check13 = threading.Thread(target=check)
check13.start()
check14 = threading.Thread(target=check)
check14.start()
check15 = threading.Thread(target=check)
check15.start()
check16 = threading.Thread(target=check)
check16.start()
