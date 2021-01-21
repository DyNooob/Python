list = ['yaj', '12345'] # list[0]为 用户名； list[1]为 密码

username = input('请输入您的用户名：')
if username == list[0]:
    print('找到此人')
    password = input('请输入密码：')
    if password == list[1]:
        print('登录成功！ 欢迎 ', list[0])
    else:
        print('密码错误')
else:
    print('没有此人')
