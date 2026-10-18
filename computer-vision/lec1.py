# import cv2 as cv
# import numpy as np
# img=np.zeros((300,300,3),dtype='uint8')
# 1. Paint an image
# img[0:100,0:]=255,0,0 #blue
# img[100:200]=0,255,0 # green
# img[200:299]=0,0,255 # red
# cv.imshow("Photo",img)
# cv.waitKey(0)
# 2.Draw a line
# cv.line(img,(0,0),(img.shape[0]//2,img.shape[1]//2),(0,255,0),thickness=2)
# cv.imshow('Line',img)
# cv.waitKey(0)
# 3.Draw a rectangle (img,pt1,pt2,color,thickness) pt=x,y
# cv.rectangle(img,(0,0),(300,100),(0,80,0),thickness=-1)
# cv.imshow('Rectangle',img)
# cv.waitKey(0)
# 4. Draw a circle (img,centre,radius,color,thickness)
# cv.circle(img,(150,150),100,(255,0,0),thickness=cv.FILLED)
# cv.imshow('Circle',img)
# cv.waitKey(0)
# 5.Write text
# cv.putText(img,"HELLO",(150,150),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
# cv.imshow('Text',img)
# cv.waitKey(0)