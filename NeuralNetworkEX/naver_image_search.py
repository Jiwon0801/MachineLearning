import requests
from urllib import request
import urllib.parse as parse
import json
import os
import re

headers = {
    "X-Naver-Client-Id" : "6XOvB9a9xjzzqCiP4ih_",
    "X-Naver-Client-Secret" : "Laksyw1aZA"
}

url = "https://openapi.naver.com/v1/search/image"

params = {
    "query" : "라이온킹",
    "start" : 1
}

res = requests.get(url, headers = headers, params = params)
print(res.status_code)

list = json.loads(res.text)
print()
for ix, item in enumerate(list["items"]):
    title = item["title"]
    link = item["link"]
    info=parse.urlparse(link)
    fileName = os.path.split(info.path)[1]
    print(ix, title, fileName)

    if not re.search(r"/.*$", fileName):
        fileName += ".jpg"

    path = "C:\Temp\donwload/{}".format(fileName)
    request.urlretrieve(link, path)


   
    



