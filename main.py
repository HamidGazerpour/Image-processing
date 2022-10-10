
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from project_functions import threshold
from project_functions import erosion
from project_functions import dilation


img = cv.imread('image1.png')
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
kernel = np.ones((5,5), np.uint8)

#Our functions
th = threshold(img_gray,120)
img_eroded = erosion(th,kernel,iterations = 1)
img_dilated = dilation(th,kernel,iterations = 1)

#OpenCV functions:
ret,CVth = cv.threshold(img_gray,120,255,cv.THRESH_BINARY)
img_CVeroded = cv.erode(CVth, kernel, iterations = 1)
img_CVdilated = cv.dilate(CVth, kernel, iterations = 1)

images = [img,th,img_eroded,img_dilated,img_gray,CVth,img_CVeroded,img_CVdilated]
titles = ['Original image','Threshold' ,'Erosion','Dilation','Grayscale image','openCV Threshold' ,'openCV Erosion','openCV Dilation']
plt.subplot(2,4,1)
plt.axis("off")
plt.title(titles[0],fontsize=8)
plt.imshow(cv.cvtColor(images[0], cv.COLOR_BGR2RGB))

for i in range(len(images))[1:]:
    plt.subplot(2,4,i+1)
    plt.axis("off")
    plt.title(titles[i],fontsize=8)
    plt.imshow(images[i],'gray')
