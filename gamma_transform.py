import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "E:\\python_tutorial\\image_processing\\college_ip\\redip\\"
    img = cv.imread(path+"factured_spin.jpg",1)
    #img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 
 #   cv.imshow('factured',img)
    
 #   cv.waitKey(0)
 #   cv.destroyAllWindows()
    
    img1 = np.power(img,1)
    img2= np.power(img,2)
    img3 = np.power(img,3)
    img4 = np.power(img,4)
    
    
    cv.imshow("img1",img)
    cv.imshow('img2',img2)
    cv.imshow('img3',img3)
    cv.imshow('img4',img4)
    
    for i in range(1,5,1):
        plt.subplot(2,2,i)
        img = np.power(img,i)
        plt.imshow(img,cmap="gray")
    
    
       
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    main()