import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def main():
    img = cv.imread("train.jfif",cv.IMREAD_COLOR)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    output = img
   
#   this is the identity matrix for the convolution
#   k = np.array([[0,0,0],[0,1,0],[0,0,0]],np.float32)
#    k = np.array(np.ones((3,3),np.float32))
    
#edge detection kernel
#  k = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],np.float32)
       
   
#blurring kernel
#   k = (1/49)*np.array(np.ones((7,7),np.float32))
  

#sharpening kernel
    k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)  
    print(k)
    print(type(k))
    
    output = cv.filter2D(img,-1,k)
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title("Original image")
    
    plt.subplot(1,2,2)
    plt.imshow(output)
    plt.title("kernel used one")    
    
                                        

    
if __name__== "__main__":
    main()  