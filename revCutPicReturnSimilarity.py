# coding:utf-8
import os
import cv2
from flask import Flask, request
from datetime import timedelta
from compareTwoCutCatFace import comparePicWithPath
from preprocessCatFace import cutFaceAndSave

app = Flask(__name__)

# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)

@app.route("/uploadBytePic",methods=["GET","POST"])
def uploadBytePic():
    fileType1 = request.form["type1"]
    fileType2 = request.form["type2"]
    
    fileobj1 = request.files['file1']
    fileobj2 = request.files['file2']
    
    pic1Bytes = fileobj1.read()
    pic2Bytes = fileobj2.read()
    
    print(type(pic1Bytes),type(pic2Bytes))
    
    pic1Name = "pic1."+fileType1
    pic2Name = "pic2."+fileType2 
    
    with open(pic1Name,"wb") as f1:
        f1.write(pic1Bytes)
    with open(pic2Name,"wb") as f2:
        f2.write(pic2Bytes)

    filename1 = pic1Name
    filename2 = pic2Name
    
    print("filename",filename1,filename2)
    
    value = comparePicWithPath(filename1,filename2)

    os.remove(filename1)
    os.remove(filename2)

    return str(value)

 
if __name__ == '__main__':
    app.run(port=5000, debug=True)





