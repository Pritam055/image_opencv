  
import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt


def main():
    img = cv.imread("train.jfif",cv.IMREAD_COLOR)
    
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    titles = ["original","Box filter" ,"Blur","Gaussin"]

    box = cv.boxFilter(img,-1,(20,20))
    
    blur = cv.blur(img,(13,13))
    
    gauss= cv.GaussianBlur(img,(37,37),0)
    
    images = [img,box,blur,gauss]
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
        
if __name__ =="__main__":
    main()