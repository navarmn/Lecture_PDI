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
img = cv2.imread('xadrez.png',cv2.IMREAD_GRAYSCALE)

    ##### Pre-sets #######################################################################
    # Load image into numpy matrix
Filter = nf.structtype()                # Cria variavel do tipo struct (similar ao matlab)

Filter.img = np.array(img)

Filter.imgSize = nf.structtype()
Filter.imgSize.lin, Filter.imgSize.col = Filter.img.shape

Filter.multiLimiar = np.array([5, 250])
Filter.multiRange = np.array([127])

# Kernel def:

numAp = 1
U = np.zeros((numAp, Filter.imgSize.lin, Filter.imgSize.col))

#############################################################################################
########### Method apllication:

for k in range(0, numAp):
    if k == 0:
        U[k, :, :] = nf.multiLimiar(Filter)
        print(U[k, :, :])
    else:
        Filter.img = U[k-1, :, :]
        U[k, :, :] = nf.multiLimiar(Filter)
        print(U[k, :, :])

#############################################################################################
########## Plot images:

########## Using matplotlib #################
plt.subplot(121), plt.imshow(img,vmin = 0, vmax = 255, cmap='gray')
plt.subplot(121).set_title('Img original')
plt.subplot(122), plt.imshow(U[(numAp - 1),:,:], vmin = 0, vmax = 255, cmap='gray')
plt.subplot(122).set_title('Img c/ aplicação de multilimiar'
                           ' %d vezes' %numAp)


plt.show()
########## Using matplotlib #################

'''
cv2.namedWindow('image 1')
cv2.imshow('image 1', img)
cv2.namedWindow('image 2')
cv2.imshow('image 2', U)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''