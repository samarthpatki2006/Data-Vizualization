import cv2 as cv
# Read and show images
# img=cv.imread('Photos/pic1.png')
# cv.imshow('P',img)
# cv.waitKey(0)

# Resize the frame (Video or photo)
# def rescaleFrame(frame,scale=5.75):
#   width=int(frame.shape[1]*scale)
#   height=int(frame.shape[0]*scale)
#   dimensions=(width,height)
#   return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# resizedImage=rescaleFrame(img)
# cv.imshow("Resized",resizedImage)
# cv.waitKey(0)

# Controlling parameters for live video
# def changeRes(width,height,brightness):
#   cap.set(3,width)
#   cap.set(4,height)
#   cap.set(10,brightness)

# Read and show Videos
# cap=cv.VideoCapture(0)
# # changeRes(640,480,180)
# while True:
#   isTrue,frame=cap.read()
#   cv.imshow("Video",frame)
#   if cv.waitKey(20) & 0xFF==ord('d'):
#     break
# cap.release()
# cv.destroyAllWindows()


