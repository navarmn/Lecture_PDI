##########################################################################################
##########################################################################################
############################################# PDI ########################################
##########################################################################################
# Just opne imagem using cv2, matplotlib e cv2
#
# Navar M M N
# 02-10-2016
##########################################################################################
##########################################################################################
# Load necessary(or not) modules
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m
import navFunc as nf
from navFunc.cls import cls

##########################################################################################
#### Open imagem:
img = cv2.imread('Escadas-small.png', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)

    ##### Pre-sets #######################################################################
    # Load image into numpy matrix
Filter = nf.structtype()                # Cria variavel do tipo struct (similar ao matlab)

Filter.img = np.array(img)

Filter.imgSize = nf.structtype()
Filter.imgSize.lin, Filter.imgSize.col = Filter.img.shape

#############################################################################################
########### Method apllication:

Hist = nf.calcHist(Filter.img)

newImage = nf.eqHist(Filter.img)
newHist = nf.calcHist(newImage)

#############################################################################################
########## Plot images:

########## Using matplotlib #################
'''
plt.figure(1)

plt.subplot(121), plt.stem(Hist)
plt.subplot(121).set_title('Histograma original')
plt.subplot(122), plt.stem(newHist)
plt.subplot(122).set_title('Histograma equalizado')

plt.figure(2)
plt.subplot(121), plt.imshow(img, vmin=0, vmax=255, cmap='gray')
#plt.subplot(121), plt.imshow(img, vmin=img.min(), vmax=img.max(), cmap='gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.imshow(newImage, vmin=newImage.min(), vmax=newImage.max(), cmap='gray')
plt.subplot(122).set_title('Imagem equalizada')

plt.show()

plt.figure(3)
plt.imshow(img, 'gray')
'''
########## Using matplotlib #################


cv2.namedWindow('image 1')
cv2.imshow('image 1', img)
cv2.namedWindow('image 2')
cv2.imshow('image 2', newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
