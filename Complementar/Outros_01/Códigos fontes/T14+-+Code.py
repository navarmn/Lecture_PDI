
# coding: utf-8

# # Introdução

# A transformação para domínios alternativos ao tempo contínuo ou discreto pode provê características importantes para análise do sinal. Em particular a transformação para o dominío da frequência utilizando a transformada de Fourier visa exibir comportamentos relativos as parte que compoem o sinal.
# 
# Qualquer sinal pode ser representado como uma soma infinita de senos e cossenos, tais componentes são chamadas de harmônicos. Então, uma análise em dominio da frequência pela transformada de fourier (também chamada de análise espectral) induz ao projetista identificar de forma direta as componentes e frequências presentes naquele sinal. Esta é uma forma de ver as menores partes presentes em um sinal.
# 
# Em relação as imagens o processamento desta transformada é traduzida matematicamente pela aplicação da seguinte transfomada no sinal:
# 
# $$F[m,n] = \frac{1}{UV} \int_o^U \int_o^V F(u,v) e^{j2\pi(um.x0 + un.y0} du dv$$

# ## Implementação e discussões

# In[1]:

import cv2
import numpy as np
import matplotlib.pyplot as plt


# - Abrir imagem:

# In[2]:

img = np.array(cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE))
rows, cols = img.shape


# - Aplicar a transformada discrea de Fourier:

# In[3]:

img_dft = np.fft.fft2(img)


# - Trazer a componente DC para o centro da imagem, transladando n/2 nas duas direções: 

# In[4]:

img_dft_shift = np.fft.fftshift(img_dft)


# - Calcular a magnitude a partir da componente real e imaginária:

# In[5]:

img_dft_mag = np.abs(img_dft_shift)


# In[6]:

plt.figure(2,figsize=(10,9))
plt.subplot(121)
plt.imshow(img, 'gray')
plt.title("Imagem original")
plt.axis('OFF')

plt.subplot(122)
plt.imshow(20*np.log(img_dft_mag), 'gray')
plt.title("Espectro em frequência")
plt.axis('OFF')

plt.show()


# - Cálculo da inversa:

# In[7]:

img_idft = np.fft.ifft2(img_dft)
img_inversa = np.abs(img_idft)

plt.figure(2)
plt.imshow(img_inversa, 'gray')
plt.title("Imagem após IDFT")
plt.axis('OFF')

plt.show()


# ## Filtragem na frequência

# ### Filtro passa-alta:

# - Criar máscara Laplaciana 

# In[8]:

def laplacianKernel(h1, h2):

    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    
    sizeKernel = np.array([h1,h2])

    kernel = -1*np.ones(sizeKernel)

    center = np.uint8(kernel.shape[0]/2)

    kernel[center,center] = (-1*np.sum(kernel)) -1
    
    return kernel

def gaussianKernel(h1, h2):

    import numpy as np
    import matplotlib.pyplot as plt
    import math as m

    ## Returns a normalized 2D gauss kernel array for general purporses

    x, y = np.mgrid[0:h2, 0:h1]
    x = x-h2/2
    y = y-h1/2
    sigma = 2
    g = np.exp( -( x**2 + y**2 ) / (2*sigma**2) )
    return g / g.sum()

filterKernel = gaussianKernel(rows,cols)


# In[9]:

filter_dft = np.fft.fft2(filterKernel)
filter_dft_shift = np.fft.fftshift(filter_dft)
filter_dft_mag = np.abs(filter_dft_shift)

filter_dft_mag = 1-filter_dft_mag

plt.figure(3+1)
plt.imshow(filter_dft_mag, 'gray')
plt.title("Espectro em frequência do filtro Gaussiano com spread 2")
plt.show()


# - Filtragem na frequência

# In[10]:

filter_img = img_dft_shift * filter_dft_mag
filter_img_mag = np.abs(filter_img)

#img_back = np.fft.fftshift(np.fft.ifft2(filter_img))

img_back = np.fft.ifft2(filter_img)

img_back_mag = np.abs(img_back)

plt.figure(5, figsize=(12,12))
plt.subplot(221)
plt.imshow((img), 'gray')
plt.title("Imagem original")

plt.subplot(222)
plt.imshow(20*np.log(img_dft_mag), 'gray')
plt.title("Espectro da imagem original")

plt.subplot(223)
plt.imshow(img_back_mag, 'gray')
plt.title("Imagem após filtragem na frequência")

plt.subplot(224)
plt.imshow(20*np.log(filter_img_mag), 'gray')
plt.title("Especto da imagem após filtragem na frequência")

plt.show()


# O filtro escolhido foi o filtro Gaussiano inverso, que funciona de forma análoga ao traidcional: atenua baixas frequências e permite a passagem de altas frequências.
# 
# O efeito na imagem é um ressalto das regiões de transições rápidas (altas frequências) promovendo um ressalto das bordas em uma imagem. Comparando os espectros é possivel notar que as regiões de constância em intensidade de cor na imagem (baixas frequências), representadas pela maior parte de informação no espectro, sofrem atenuações e o resultado é um novo espectro com um aspecto limpo, exaltando apenas componentes de alta frequência e menos presente na imagem.

# # Conclusões

# A análise de imagens no domínio da frequência é uma ferramenta que provê análises visuais perante a imagem, exibe padrões de comportamento das cores na imagem, podem resultar em identificação de componentes como ruído ou objetos ao olhar para o espectro.
# 
# Há a possibilidade de realizar filtragem no domínio da frequência, assim no domínio temporal, é um processa mais rápido pois envolve uma multiplica simples ponto a ponto, talvez o grande parte do custo computacional em executar tal técnica está em realizar a transformada direta e inversa de Fourier.
