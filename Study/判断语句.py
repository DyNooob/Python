age_1 = 20
age_2 = 16

msg_1 = age_1 > 18 and '成年' or '未成年'

print(msg_1)

msg_2 = '成年' if age_2 > 18 else '未成年'

print(msg_2)

msg_3 = ('成年', '未成年')[age_2 > 18] # (false, true)[condition]

print(msg_3)

msg_4 = (lambda: '成年',lambda: '未成年')[age_2 > 18]()# >(lambda: <on_false>, lambda:<on_true>)[<condition>]()

print(msg_4)


msg_5 = {True: '成年', False: '未成年'}[age_2 > 18]# {True: <on_true>, False: <on_false>}[<condition>]

print(msg_5)