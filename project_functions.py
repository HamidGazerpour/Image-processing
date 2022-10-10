#We defined 3 functions (threshold,erosion,dilation) in this file

import numpy as np

def dilation(img,kernel,iterations):
    dilated = img.copy()
    height, width = img.shape[:2]
    h_kernel, w_kernel = kernel.shape[:2]
    for it in range(iterations):
        img = dilated.copy()
        for i in range(height):
            for j in range(width):
                s=0
                for k in np.arange(-h_kernel//2,h_kernel//2,1):
                    for m in np.arange(-h_kernel//2,h_kernel//2,1):
                        if i+k>=0 and j+m>=0 and (i+k)<height and (j+m)<width:
                            if img[i+k,j+m]==255:
                                s=1
                                if s==1:
                                    dilated[i,j]=255
    return dilated

def erosion(img,kernel,iterations):
    eroded = img.copy()
    height, width = img.shape[:2]
    h_kernel, w_kernel = kernel.shape[:2]
    for it in range(iterations):
        img = eroded.copy()
        for i in range(height):
            for j in range(width):
                s=0
                for k in np.arange(-h_kernel//2,h_kernel//2,1):
                    for m in np.arange(-h_kernel//2,h_kernel//2,1):
                        if i+k>=0 and j+m>=0 and (i+k)<height and (j+m)<width:
                            if img[i+k,j+m]==0:
                                s=1
                                if s==1:
                                    eroded[i,j]=0
    return eroded        

def threshold(img,thres):
    img_thres = img.copy()
    height, width = img.shape[:2]
    for i in range(height):
        for j in range(width):
            if img_thres[i,j] >= thres:
                img_thres[i,j]=255
            else:
                img_thres[i,j]=0

            
    return img_thres        