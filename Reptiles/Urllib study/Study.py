import ssl
from urllib import parse, request

context = ssl._create_unverified_context()
data = {
    "name": "admin",
    "password": "Dy2005125"

}
data = bytes(parse.urlencode(data),'utf-8')
HTTPResponse = request.Request("http://blog.nooob.top/admin/", data=data, method='POST')
response = request.urlopen(HTTPResponse,context=context)
print(response.read().decode("utf-8"))