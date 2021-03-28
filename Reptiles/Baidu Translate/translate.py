import urllib.parse
import requests
import jsonpath
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS'
}


def url_():
  key_words = input("输入您要翻译的内容: ")
  url = "https://fanyi.baidu.com/sug?kw={}".format(key_words)
  return url


def request_data():
  url = url_()
  res = requests.get(url, headers=headers)
  json_data = json.loads(res.text)
  # print(json_data)
  useful_data = jsonpath.jsonpath(json_data, '$..v')
  direct_data = useful_data[0].replace(';', '\n').replace(' ', '')
  print('-'*10, '\n', direct_data, '\n', '-'*10)


if __name__ == "__main__":
  request_data()

