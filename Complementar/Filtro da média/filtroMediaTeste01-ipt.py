
# coding: utf-8

# # Aplicações e avaliações do Filtro da Média

# ## Implementação

# 

# In[ ]:

Impor


# In[9]:

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m
import navFunc as nf
from navFunc.cls import cls


# In[10]:

img = cv2.imread('lena.png',cv2.IMREAD_GRAYSCALE)


# In[11]:

Filter = nf.structtype()                # Cria variavel do tipo struct (similar ao matlab)

Filter.img = np.array(img)

Filter.imgSize = nf.structtype()
Filter.imgSize.lin, Filter.imgSize.col = Filter.img.shape
#################### Filtro da média
Filter.ftype = 1;

# Kernel def:

Filter.kernelSize = 3
Filter.kernel = np.ones((Filter.kernelSize, Filter.kernelSize))

numAp = 1;
U = np.zeros((numAp, Filter.imgSize.lin, Filter.imgSize.col))

#############################################################################################
########### Method apllication:

for k in range(0, numAp):
    if k == 0:
        U[k,:,:] = nf.filterMean(Filter)
        print(U[k, :, :])
    else:
        Filter.img = U[k-1,:,:]
        U[k, :, :] = nf.filterMean(Filter)
        print(U[k,:,:])

#############################################################################################
########## Plot images:

########## Using matplotlib #################
plt.subplot(121), plt.imshow(img, 'gray')
plt.subplot(121).set_title('Img original')
plt.subplot(122), plt.imshow(U[(numAp - 1),:,:], 'gray')
plt.subplot(122).set_title('Img c/ aplicação do filtro da média %d vezes' %numAp)


plt.show()


# In[ ]:




# In[ ]:



