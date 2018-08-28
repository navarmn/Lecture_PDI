
# coding: utf-8

# # Introdução

# Os métodos e estudos de morfologia matemática inicialmente desenvolvidos para imagens binárias apresentam caracaterísticas imporatantes em aplicação em imagens tons de cinza. A operação dos métodos é mantida, porém neste caso as aplicações visam reduzir, ruídos, ressaltar bordas, destacare componentes, além de outros resultados.
# 
# Entretanto há um destaque para o método do gradiente morfológico, que utiliza a combinação entre erosão e dilatação para promover ressalto das bordas de uma imagem, da seguinte forma:
# $$ g = (f\oplus b) - (f \ominus b) $$

# # Discussões sobre os métodos

# A operação do gradiente mofológico funciona como uma filtragem passa-alta no dominio do tempo, ressaltando bordas e removendo regiões homogêneas. O operador de erosão funciona diminuindo as regiões com tons brancos, enquanto ao mesmo tempo a dilatação aumenta as regiões brancas, a subtração desses efeitos resultado nas bordas da imagem, como a seguir:

# In[1]:

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt


# - Abrir imagem:

# In[2]:

img = np.array(cv2.imread('house.tif'))

plt.figure(1)
plt.imshow(img)
#plt.axis("off")
plt.title("Imagem original")
plt.show()


# ### Gradiente Morfológico:

# - Elementro Estruturante 01:

# In[3]:

sizeEE = (5,5)

kernel = cv2.getStructuringElement(0, sizeEE, (-1,-1))
print(kernel)


# In[4]:

img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# In[5]:

plt.figure(2,figsize=(12,12))
plt.subplot(131)
plt.imshow(img)
plt.axis("off")
plt.title("Imagem original")

plt.subplot(132)
plt.imshow(img_gradient)
plt.axis("off")
plt.title("Imagem após gradiente morfológico")

plt.subplot(133)
plt.imshow(kernel, 'gray', interpolation='nearest')
plt.axis("off")
plt.grid()
plt.title("El. Estruturante")
plt.show()


# - Elementro Estruturante 02:

# In[6]:

sizeEE = (5,5)

kernel = cv2.getStructuringElement(1, sizeEE, (-1,-1))
print(kernel)


# In[7]:

img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# In[8]:

plt.figure(3,figsize=(10,9))
plt.subplot(131)
plt.imshow(img)
plt.axis("off")
plt.title("Imagem original")

plt.subplot(132)
plt.imshow(img_gradient)
plt.axis("off")
plt.title("Imagem após gradiente morfológico")

plt.subplot(133)
plt.imshow(kernel, 'gray', interpolation='nearest')
plt.axis("off")
plt.grid()
plt.title("El. Estruturante")
plt.show()


# - Elementro Estruturante 03:

# In[9]:

sizeEE = (5,5)

kernel = cv2.getStructuringElement(2, sizeEE, (-1,-1))
print(kernel)


# In[10]:

img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# In[11]:

plt.figure(3+1, figsize=(12,12))
plt.subplot(131)
plt.imshow(img)
plt.axis("off")
plt.title("Imagem original")

plt.subplot(132)
plt.imshow(img_gradient)
plt.axis("off")
plt.title("Imagem após gradiente morfológico")

plt.subplot(133)
plt.imshow(kernel, 'gray', interpolation='nearest')
plt.axis("off")
plt.grid()
plt.title("El. Estruturante")
plt.show()


# Os diferentes tipos de elementos estruturante promovem ressalto das bordas nas regiões de crescimento ou retração do elemento.

# # Conclusões

# A utilização do gradiente morfológico para destacar bordas é equivalente a filtragem passa-alta no domínio espacial ou da frequência. A vatangem para tal método está no custo computacional menor que para implementação de tais filtros.
