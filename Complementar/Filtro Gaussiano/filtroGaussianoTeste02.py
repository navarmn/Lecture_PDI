3##########################################################################################
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
img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)

    ##### Pre-sets #######################################################################
    # Load image into numpy matrix
Filter = nf.structtype()                # Cria variavel do tipo struct (similar ao matlab)

Filter.img = np.array(img)

Filter.imgSize = nf.structtype()
Filter.imgSize.lin, Filter.imgSize.col = Filter.img.shape
#################### Filtro da média
Filter.ftype = 1;

# Kernel def:

kernels = np.array([3, 5, 7, 9, 11, 15, 17])

numAp = 1;

# Variável auxiliar para guardar a saída
U = np.zeros((numAp, Filter.imgSize.lin, Filter.imgSize.col, kernels.size))

for l in range(0, kernels.size):

    Filter.kernelSize = kernels[l]

    Filter.kernel = np.ones((Filter.kernelSize, Filter.kernelSize))

#############################################################################################
########### Method apllication:

    for k in range(0, numAp):
        if k == 0:
            U[k, :, :, l] = nf.filterGaussian(Filter)
            print(U[k, :, :, l])
        else:
            Filter.img = U[k-1, :, :]
            U[k, :, :, l] = nf.filterGaussian(Filter)
            print(U[k, :, :, l])

#############################################################################################
########## Plot images:

########## Using matplotlib #################
plt.figure(1)
plt.imshow(img, 'gray')
plt.title('Imagem original')

plt.figure(2)
plt.imshow(U[(numAp - 1),:,:,0], 'gray')
plt.title('Kernel 3x3')

plt.figure(3)
plt.imshow(U[(numAp - 1),:,:,1], 'gray')
plt.title('Kernel 5x5')

plt.figure(3+1)
plt.imshow(U[(numAp - 1),:,:,2], 'gray')
plt.title('Kernel 7x7')

plt.figure(5)
plt.imshow(U[(numAp - 1),:,:,3], 'gray')
plt.title('Kernel 9x9')

plt.figure(6)
plt.imshow(U[(numAp - 1),:,:,(3+1)], 'gray')
plt.title('Kernel 11x11')

plt.figure(7)
plt.imshow(U[(numAp - 1),:,:,5], 'gray')
plt.title('Kernel 15x15')

plt.figure(8)
plt.imshow(U[(numAp - 1),:,:,6], 'gray')
plt.title('Kernel 17x17')

plt.show()


'''
plt.subplot(121), plt.imshow(img, 'gray')
plt.subplot(121).set_title('Img original')
plt.subplot(122), plt.imshow(U[(numAp - 1),:,:], 'gray')
plt.subplot(122).set_title('Img c/ aplicação do filtro da Sobel %d vezes' %numAp)
'''

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