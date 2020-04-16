import cv2 as cv
import matplotlib.pyplot as plt
 
def main():
    path = "E:\\python_tutorial\\image_processing\\college_ip\\redip\\standard_test_images\\"
    img = cv.imread(path+"cameraman.tif",0)
 #   img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    th = 0
    max_val = 255
    
    #in complex times the process of automatic getting the threshold value for the correct speeration of the object then we use OTSU with our used threshold model and for this we will set th=0
    ret,o1 = cv.threshold(img,th,max_val,cv.THRESH_BINARY +cv.THRESH_OTSU)
    ret,o2 = cv.threshold(img,th,max_val,cv.THRESH_BINARY_INV +cv.THRESH_OTSU)
    ret,o3 = cv.threshold(img,th,max_val,cv.THRESH_TOZERO +cv.THRESH_OTSU)
    ret,o4 = cv.threshold(img,th,max_val,cv.THRESH_TOZERO_INV +cv.THRESH_OTSU)
    ret,o5 = cv.threshold(img,th,max_val,cv.THRESH_TRUNC +cv.THRESH_OTSU)
    
    output = [img,o1,o2,o3,o4,o5]
    titles = ['Original','Binary','Binary_inv','Zero','Zero Inv','Trunc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.title(titles[i])
        plt.imshow(output[i],cmap='gray')
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
        
if __name__=="__main__":
    main()  
    
    