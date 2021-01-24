import zipfile

# 生成六位数密码字典(测试使用，密码是六位纯数字)
# f = open('password.txt', 'w')
# for id in range(1000000):
#     password = str(id).zfill(6) + '\n'
#     f.write(password)
#
# f.close()


def done(pwd):
    print("OK, Password is :", pwd)
    f = open('pwd.txt', 'w')
    f.write(pwd)
    exit(200)


def pwd_file(zipFile, password):
    try:
        zipFile.extractall(pwd=bytes(password, 'utf8'))
        done(password)
    except:
        print("Password: ", password, " wrong")


def main():
    zipFile = zipfile.ZipFile('./test.zip')
    pwd_list = open("./password.txt")
    for line in pwd_list.readlines():
        pwd = line.strip('\n')
        pwd_file(zipFile, pwd)


if __name__ == '__main__':
    main()
