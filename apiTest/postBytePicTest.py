# -*- coding: utf-8 -*-

import requests


#将图片按字节流存储
with open(r"1_1.jpg","rb") as f:
    file1 = f.read()
with open(r"1_2.jpg","rb") as f:
    file2 = f.read()

data = {}
files = {}
data["type1"] = "jpg"
data["type2"] = "jpg"
files["file1"] = file1
files["file2"] = file2

#r = requests.post("http://148.70.167.241:5000/uploadBytePic",files=files,data=data)
r = requests.post("http://127.0.0.1:5000/uploadBytePic",files=files,data=data)

print(r.status_code)

if(r.status_code == 200):
    print(r.text)