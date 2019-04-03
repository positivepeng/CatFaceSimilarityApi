# -*- coding=utf-8 -*-
import cv2

def cutFaceAndSave(path,showIt = False):
	# 加载猫脸检测器
	catPath = "haarcascade_frontalcatface.xml"
	faceCascade = cv2.CascadeClassifier(catPath)

	# 读取图片并灰度化
	img = cv2.imread(path)  
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# 猫脸检测
	#1.image——输入图像
    #2.scaleFactor——表示每轮检测图像齿轮减少的比例
    #3.minNeighbors——指明对象要至少被检测到几次才能判定对象确实存在
    #4.minSize——检测对象的最小尺寸
    #5.maxSize——检测对象的最大尺寸
	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor= 1.02,
	    minNeighbors=3,
	    minSize=(150, 150),
	    flags=cv2.CASCADE_SCALE_IMAGE
	)
	maxRectangle = 0
	xx,yy,ww,hh = 0,0,0,0

	for (x,y,w,h) in faces:
		if w * h > maxRectangle:
			xx = x
			yy = y
			ww = w
			hh = h
			maxRectangle = w * h

	#如果检测到则截取，保存图片
	if(maxRectangle > 0):
		crop_img = img[yy:(yy+hh),xx:(xx+ww)] 
		cv2.imwrite(path,crop_img)

	if showIt:
		# 框出猫脸并加上文字说明
		cv2.rectangle(img, (xx, yy), (xx+ww, yy+hh), (0, 0, 255), 2)
		cv2.putText(img,'Cat',(xx,yy-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

		# 显示图片并保存
		cv2.namedWindow("Cat",0);
		cv2.resizeWindow("Cat", 500, 500); 
		cv2.imshow('Cat', img)
		c = cv2.waitKey(0)


if __name__ == '__main__':
	path = "./images/8.jpg"
	cutFaceAndSave(path,showIt=True)
