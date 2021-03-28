import sys
import hashlib
import importlib

file_name = "E:\ISO\Vmware Installer macOS Catalina(19A603).cdr"
 
d5 = hashlib.md5()
with open(file_name,'rb') as f:
  while True:
      data = f.read(2024)
      if not data:
          break
      d5.update(data)
print(d5.hexdigest())