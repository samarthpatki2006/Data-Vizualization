# import cv2 as cv
# img=cv.imread('Photos/pic2.png')
# # 0. Resizing
# img=cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
# cv.imshow('Resize',img)
# 1 Convert to gray scale
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
# cv.waitKey(0)
# 2.Bluring
# blur=cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)
# 3. Edge
# cany=cv.Canny(img,125,175)
# cv.imshow('Edge',cany)
# 4.Dilations (thicken the edges)
# dilated=cv.dilate(cany,(3,3),iteration=1)
# cv.imshow('Dilated',dilated)
# 5. Erode (get back to cany from dilated)
# erode=cv.erode(dilated,(3,3),iteration=1)
# cv.imshow('Eroded',erode)
# 6 Cropping
# cropped=img[100:200,0:300]
# cv.imshow('Cropped',cropped)
# cv.waitKey(0)