# Python 3 com OpenCV 3

[Python](https://www.python.org/) é uma das linguagem de uso geral e uma das mais populares do momento. Bastante usada no meio acadêmico, científico e na ciência de dados. 

Pode ser usada para uma diversa gama de aplicações e é totalmente escalável. Vem nativamente no Linux (*e.g.* Ubuntu >= 17 vem com python 3 nativo, também).

**Vantagem**
+ Trabalhar e se familiarizar com a [linguagem mais bem paga](https://qz.com/298635/these-programming-languages-will-earn-you-the-most-money/) de 2018 (salário médio de $116.128 por ano)
+ Full review em dos dados de [QZ](https://qz.com/298635/these-programming-languages-will-earn-you-the-most-money/) e [TIOBE](https://www.tiobe.com/tiobe-index/) em: [Link 1](https://medium.com/@ChallengeRocket/top-10-of-programming-languages-with-the-highest-salaries-in-2017-4390f468256e), [Link 2](https://www.youtube.com/watch?v=f3EbDbm8XqY&t=515s).
+ Transformar os seu projeto da disciplina em um produto e apresentar no seu portfolio (Github) :).

## Instalação

Se você for utilizar python para desenvolver seus projetos, recomendo a instalação da distribuição Anaconda. Essa é uma distribuição cientifica do python que já vem por default com ~~quase~~ todos os pacotes necessários para começar a programar. Faça o download [aqui](https://www.anaconda.com/download/).

**Importante**:
> Aceite o python do anaconda como principal (**base**). Isso será perguntando no início da instalação.

Para transformar o python um ambiente para processamento de imagens deve-se utilizar a biblioteca [OpenCV](https://opencv.org/).

**NÃO instale a OpenCV pelo link: https://docs.opencv.org/master/da/df6/tutorial_py_table_of_contents_setup.html**, pois irá instalar a biblioteca no Python 2 (se você tiver.)

Para instalar a OpenCV 3.xx no Python 3, instale a `opencv-python`, seguindo as [instruções](https://pypi.org/project/opencv-python/).

## IDE - ambiente para simulaçao

Há diversas opções. Cada uma possui vantagens e desvantagens. A escolha é muito pessoal e cabe ao programar testar e identificar qual lhe convém melhor. As principais opções são:

+ [JupyterLab ou Jupyter Notebook](http://jupyter.org/): já vem com a Anaconda. Para usar abra o **terminal**, ou **cmd** e digite: `jupyter lab` ou `jupyter notebook`.

> É de longe a opção mais escolhida por cientista de dados, pois oferece um ambiente iterativo para criar progrmas na forma de relatório e ótimo para exibir imagens e dados.

+ [Spyder](https://pythonhosted.org/spyder/index.html): já vem com a Anaconda. Para usar abra o **terminal**, ou **cmd** e digite: `spyder`.

> É uma tentativa de criar uma ambiente do python parecido com o Matlab e Octave.

+ [Pycharm](https://www.jetbrains.com/pycharm/): Deve ser instalada depois do python.
> IDE muito boa, com todos os recursos necessários já na versão free. Possui ferramentas para debug, visualização de variáveis, objetos, etc. Suporte para git e [ambientes virtuais](https://realpython.com/python-virtual-environments-a-primer/).

+ Editores diversos: [Sublime](https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/), [Atom](https://stackoverflow.com/questions/35546627/how-to-configure-atom-to-run-python3-scripts), [Visual Code](https://code.visualstudio.com/docs/languages/python).


As simulações executadas na aula serão feitas no jupyter notebook, e os scripts estão na mesma pasta desse material.

As imagens utilizadas para as simulações estarão na pasta de [Figuras](../figs)

## Carregar, exibir imagem e converter entre tipos:

O [notebook 01](notebook_01__how_to.ipynb) contém as descrições exibidas a seguir.

### Para iniciar

Antes de iniciar qualquer script em python deve-se importar os módulos nécessários. Para os primeiros trabalhos de pdi os principais serão: OpenCV, Numpy e Matplotlib. Devem ser chamados da seguinte forma:

```python
import cv2 #OpenCV
import numpy as np #biblioteca para trablahar com arrays de forme eficiente
import matplotlib.pyplot as plt # biblioteca para plotar gráficos
``` 

#### Dica
> Sempre procurar a documentação das bibliotecas.
> + OpenCV: [aqui](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html).
> + Numpy: [aqui](https://docs.scipy.org/doc/numpy/user/quickstart.html).
> + Matplotlib: [aqui](https://matplotlib.org/tutorials/index.html).

### Função `cv2.imread`

```python
img = cv2.imread('../figs/lena_color_256.tif')
``` 

### Função `cv2.imshow` e `plt.imshow`

```python
cv2.imshow('Image', img)
plt.imshow(img)

``` 

## Histograma

Para essa parte, use o [notebook 02](notebook_02__histogram.ipynb), pois conterá as simulações exibidas a seguir.

[como fazer com a OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html?highlight=hist)

[Algumas plotagens em imagens](https://matplotlib.org/users/image_tutorial.html)


### Outras funções básicas:

**Arrays**

+ `np.shape` - grava uma imagem
+ `imagesc` - re-escala e exibe
+ `colorbar` - coloca um eixo de cores
+ `getimage` - pega a imagem do eixo
+ `truesize` - mostra em tamanho real




## Documentação

### OpenCV

* https://docs.opencv.org/3.4/
* https://opencv-python-tutroals.readthedocs.io/en/latest/index.html