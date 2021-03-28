from pymouse import PyMouse
import time

m = PyMouse()
print(m.position())
check_time = input('请输入点击次数（大约需要8000次）：')
check_time = int(check_time)
time_sleep = input('请输入秒数，回车后将开始暂停此秒数后开始点击：')
time_sleep = int(time_sleep)

time.sleep(time_sleep)
for a in range(1, check_time):
    m.click(858, 603, 1)
    time.sleep(0.0001)
    print(a)
    if a == check_time:
        break
# written by DY
# DYblog
# e-mail:duyun888888@qq.com
