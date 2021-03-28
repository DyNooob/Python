import hashlib
while True:
  content = input("Enter text: ")
  md5hash = hashlib.md5(content.encode("utf-8"))
  md5 = md5hash.hexdigest()
  print("'", content, "'", "md5 value is:", md5)