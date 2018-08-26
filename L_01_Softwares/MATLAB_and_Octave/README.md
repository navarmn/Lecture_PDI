# Matlab e Octave

Para a utilização dessas ferramentas é necessário que elas tenham sido previamente instaladas em suas máquinas. 
O *Octave* é distribuído de forma livre e pode ser feito download [aqui](https://www.gnu.org/software/octave/). O *MATLAB*, por outro lado, possui licensa proprietária.

A similaridade entre os programas é tanta que as principais funções internas de ambos os softwares são praticamente intercambiáveis. 

#### Importante

> O Octave por padrão não veem com a biblioteca de processamento de imagem instaladas. Elas devem ser instaladas após o Octave. A biblioteca para processamento de imagens está disponível [aqui](https://octave.sourceforge.io/image/index.html).

> Como instalar bibliotecas do Octave no [Windows](https://octave.org/doc/v4.2.2/Installing-and-Removing-Packages.html) e [Linux](https://askubuntu.com/questions/685038/how-can-i-install-a-package-from-octave-forge).

> Lista de [todas as bibliotecas do Octave](https://octave.sourceforge.io/packages.php).

As simulações executadas na aula serão feitas no MATLAB, e as funções e scripts equivalente serão exibidos no Octave.

As imagens utilizadas para as simulações estarão na pasta de [Figuras](../figs)

## Carregar, exibir imagem e converter entre tipos:

O [script 01](script_01__load_image.m) contém as descrições exibidas a seguir.

### Função `imread`
 
Carregar a imagem para uma matriz. A matriz de saída é uma variável que possui valores discretizados de acordo com os níveis de cinza da imagem. Exemplo:

```matlab
% Load image to a variable.
img = imread('../figs/lena_color_512.tif');
```
**Importante:** o MATLAB e Octave realizam cálculos matriciais. Observe o tamanho da variável de saída (matriz *n*-dimensional). 

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
imshow(img)
```

**Funções úteis:**
+ `figure` - cria instâncias adicionais para visualizar a imagem. Chame sempre antes de chamar `imshow` ou `image`
+ `subplot` - para exibir imagens em formato de grade (dispostas ao lado ou abaixo em uma mesma figura).

### Função `rgb2gray`

```matlab
rgb2gray(img)
```

### Outras funções básicas:

**Saída**

+ `imwrite` - grava uma imagem
+ `imagesc` - grava uma imagem
+ `colorbar` - grava uma imagem
+ `getimage` - grava uma imagem
+ `truesize` - grava uma imagem



**Outras conversões:**

+ `gray2ind`
+ `im2bw`
+ `im2double`
+ `im2uint8`
+ `im2uint16`
+ `ind2gray`
+ `mat2gray`
+ `rgb2gray` 
+ `rgb2ind`


# Referências
<a href="https://www.mathworks.com/help/matlab/ref/rgb2gray.html" target="_blank"></a>
