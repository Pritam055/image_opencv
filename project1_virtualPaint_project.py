import cv2
import numpy as np

frameWidth = 1000
frameHeight = 1000
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth) #width id no. 3
cap.set(4,frameHeight) #height id no. 4
cap.set(10,150) # change brightness whose id no. is 10

myColors = [[0,121,223,179,255,255],[116,108,88,179,255,255]] #orange,pink

colorValues = [[51,153,255],[133,21,199]] #orange

myPoints =[] #[x, y, colorId]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        # cv2.imshow("img",mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,width,height=0,0,0,0
    for cnt in contours:
      area = cv2.contourArea(cnt)
      if area>500:
          # print(area)
          cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
          peri = cv2.arcLength(cnt,True)
          approx = cv2.approxPolyDP(cnt,0.02*peri,True)
          x,y,width,height = cv2.boundingRect(approx)
    return x+width//2,y #this give the top and center points
# The functions approxPolyDP approximate a curve or a polygon with another curve/polygon with less vertices so that the distance between them is less or equal to the specified precision.

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),6,myColorValues[point[2]],cv2.FILLED)

while True:
    success,img = cap.read()
    imgResult = img.copy() #this image will be final one with result
    newPoints = findColor(img,myColors,colorValues)
    if len(newPoints)!=0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,colorValues)
    cv2.imshow('imgResult',imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()