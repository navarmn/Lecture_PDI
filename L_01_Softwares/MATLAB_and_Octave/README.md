# Matlab e Octave

Para a utilização dessas ferramentas é necessário que elas tenham sido previamente instaladas em suas máquinas. 
O *Octave* é distribuído de forma livre e pode ser feito download [aqui](https://www.gnu.org/software/octave/). O *MATLAB*, por outro lado, possui licensa proprietária.

A similaridade entre os programas é tanta que as principais funções internas de ambos os softwares são praticamente intercambiáveis. 

As simulações executadas na aula serão feitas no MATLAB, e as funções e scripts equivalente serão exibidos no Octave.

As imagens utilizadas para as simulações estarão na pasta 

## Carregar imagens:

##### Dica
> Sempre usar o *help* do MATLAB ou Octave.

> Pode ser chamado da seguinte forma:

> 1. `doc` no terminal interno.
> 2. [https://www.mathworks.com/help/matlab/](Documentação online).
> 3. Chamando o comando `help` na função que deseja saber como funciona.

```matlab
clc
clear all
close all

%% Load image:

% Load image to a variable.
img = imread('../figs/lena_color_512.tif');

% Show images in two ways:
figure;
image(img)

figure;
imshow(img)

```
