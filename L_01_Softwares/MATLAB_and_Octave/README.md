# Matlab e Octave

Para a utilização dessas ferramentas é necessário que elas tenham sido previamente instaladas em suas máquinas. 
O *Octave* é distribuído de forma livre e pode ser feito download [aqui](https://www.gnu.org/software/octave/). O *MATLAB*, por outro lado, possui licensa proprietária.

A similaridade entre os programas é tanta que as principais funções internas de ambos os softwares são praticamente intercambiáveis. 

As simulações executadas na aula serão feitas no MATLAB, e as funções e scripts equivalente serão exibidos no Octave.

As imagens utilizadas para as simulações estarão na pasta 

## Carregar e exibir imagem:

O [script 01](script_01__load_image.m) contém as descrições exibidas a seguir.

### Função `imread`
 
Carregar a imagem para uma matriz. A matriz de saída é uma variável que possui valores discretizados de acordo com os níveis de cinza da imagem. Exemplo:

```matlab
% Load image to a variable.
img = imread('../figs/lena_color_512.tif');
```
**Importante:**o MATLAB e Octave realizam cálculos matriciais. Observe o tamnho da variável de saída (matriz *n*-dimensional). 

**Funções úteis:**
+ `size` - retorna tamanho da variável.


#### Dica
> Sempre usar o *help* do MATLAB ou Octave.

> Pode ser chamado da seguinte forma:

> 1. `doc` no terminal interno.
> 2. [https://www.mathworks.com/help/matlab/](Documentação online).
> 3. Chamando o comando `help` na função que deseja saber como funciona.

### Função `ìmshow` e `image`

Não há diferenças tangíveis, use a que for mais conveniente.


```matlab
figure;
image(img)
```

**Funções úteis:**
+ `figure` - cria instâncias adicionais para visualizar a imagem. Chame sempre antes de chamar `imshow` ou `image`
+ `subplot` - para exibir imagens em formato de grade (dispostas ao lado ou abaixo em uma mesma figura).




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


# Referências
<a href="https://www.mathworks.com/help/matlab/ref/rgb2gray.html" target="_blank"></a>
