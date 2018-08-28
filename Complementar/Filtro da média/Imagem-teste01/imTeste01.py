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
# Load necessary module
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m

import time
##########################################################################################
# Open imagem:

img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)

# Load image into numpy matrix

A = np.array(img)

class structtype():
    pass

size = structtype()
size.A = structtype()

#B = A[1:5,1:5]
B = A

size.A.lin, size.A.col = B.shape


#################### Filtro da média
# Kernel def:

size.kernel = structtype()

kernelSize = 3
kernel = np.ones((kernelSize, kernelSize))

size.kernel.lin, size.kernel.col = kernel.shape
central = int((size.kernel.lin/2))

#

C = np.zeros((size.A.lin + central*2,size.A.col + central*2))
C[(0 + central):(size.A.lin + central), (0 + central):(size.A.col + central)] = B

# Run matrix
soma = 0;
D = np.zeros(B.shape)

for j in range((0),size.A.lin):
    for k in range((0), size.A.col):
        # Run kernel in one matrix's elements
        for kl in range(0, kernelSize):
            for kk in range(0, kernelSize):

                #print(C[j + kl, k + kk])
                #print(kernel[kl, kk])
                #print('Result is: %d ' %(C[j + kl,k + kk] * kernel[kl,kk]))

                soma = (C[j + kl, k + kk] * kernel[kl, kk]) + soma

       # print('Pixel has finished')
        value = m.ceil((soma/kernel.size))
        soma = 0
        D[j,k] = value
    #print('LINE has finished')

D = np.uint8(D)

# Plot image
'''
plt.imshow(A, cmap='gray')
plt.figure(1)
plt.show()
'''

#cv2.namedWindow('image 1')
cv2.imshow('image 1', img)
#cv2.namedWindow('image 2')
cv2.imshow('image 2', D)
cv2.waitKey(0)
cv2.destroyAllWindows()
