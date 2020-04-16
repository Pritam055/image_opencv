
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as polt

def main():
    path = "E:\\python_tutorial\\image_processing\\college_ip\\redip\\"
    
    img1 = path+"gradient.jpg" 
    
    img1= cv.imread(img1,1)
    
    
    ret,o1 = cv.threshold(img1,50,255,cv.THRESH_BINARY)
    ret,o2 = cv.threshold(img1,50,255,cv.THRESH_BINARY_INV)
    ret,o3 = cv.threshold(img1,127,255,cv.THRESH_TOZERO)
    ret,o4 = cv.threshold(img1,127,255,cv.THRESH_TOZERO_INV)
    ret,o5 = cv.threshold(img1,127,255,cv.THRESH_TRUNC)
    
    images = [img1,o1,o2,o3,o4,o5]
    titles = ['img1','Binary','Binary Inv','ToZero','ToZero_inv','Trunc']
    
    for i in range(len(images)):
        plt.subplot(2,3,i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
        
 
        
    
if __name__=="__main__":
    main()
    