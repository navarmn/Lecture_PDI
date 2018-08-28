
# coding: utf-8

# # Introdução

# Um outra ferramenta para análise no domínio da frequência é a transformada Wavelet. A operação desta transformada é realizada pela convolução com um sinal previamente conhecido, e o resultado, diferente da transformada de Fourier representa uma semelhança entre o sinal de entrada e o sinal usado como base.
# 
# Dentre as funções base para a transformada Wavelet, detaca-se o operador Haar, que utiliza sinais quadrados de frequência fixas para extrair informações pertinentes ao sinal. A representação matemática dar-se da seguinte forma:
# 
# $$ T = HFH $$
# 
# F é a matriz de entrada, H a matriz wavelet e T o resultado da trasnformada.

# # Discussão do método

# O método da transformada Wavelet, com funções de base Haar extrair informações presentes na imagem e promover uma compressão do sinal.

# In[1]:

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt


# - Abrir imagem:

# In[2]:

img = np.array(cv2.imread('lena-big.png', cv2.IMREAD_GRAYSCALE))

plt.figure(1)
plt.imshow(img, 'gray')
plt.title("Imagem original")
plt.show()


# - Aplicar a transformada discreta com Wavelet de base Haar:

# In[3]:

img_haar = pywt.dwt2(img, 'haar')


# In[4]:

cA, (cH, cV, cD) = img_haar


# In[5]:

print('Resultados:')
print(cA.shape)
print(cH.shape)
print(cV.shape)
print(cD.shape)


# In[6]:

plt.figure(2,figsize=(12,12))

plt.subplot(221)
plt.imshow(cA, 'gray')
plt.title('Imagem original')
plt.subplot(222)
plt.imshow(cH, 'gray')
plt.title('Imagem horizontais')
plt.subplot(223)
plt.imshow(cV, 'gray')
plt.title('Imagem verticais')
plt.subplot(224)
plt.imshow(cD, 'gray')
plt.title('Imagem diagonais')
plt.show()


# O resultado da transformada de haar são três subprodutos da imagem original, implementados da seguinte forma: (i) a imagem original passa por uma filtragem passa-alta resultando em três imagens, chamadas de coeficientes, com informações pertinentes a linhas horizontais, verticais e diagonais; (ii) após isso as imagens passam por uma filtragem passa-baixa, com o intuito de preservar as características originais e por fim (iii) passam por um processo de downscalling.

# # Conclusões

# A transformada Haar pode ser uma ferramenta útil quando trata-se de compreensão de imagens, pois as informações extraídas com a aplicação desssa transformada são de aproximações e predições da imagem original, sofrendo um processo de redução de dimensionailidade.
