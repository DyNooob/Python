while True:
  imyear = input("请输入您的出生月份: ")
  if 0 < int(imyear) <= 3:
    print("您在春天出生")
  if 3 < int(imyear) <= 6:
    print("您在夏天出生")
  if 6 < int(imyear) <= 9:
    print("您在秋天出生")
  if 9 < int(imyear) <=12:
    print("您在冬天出生")
  if int(imyear) >= 13:
    print("月份错误，请再重新输入")
  if int(imyear) <=0:
    print("月份错误，请再重新输入")