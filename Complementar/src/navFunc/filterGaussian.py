def filterGaussian (Filter):
    ### Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    import navFunc as nf

    # Load image into numpy matrix

    A = Filter.img

    size = nf.structtype()
    size.A = nf.structtype()
    size.A.lin, size.A.col = A.shape

    #################### Gaussian filter
    ## Pre-set steps:
    ### Generate two kernersl (horizontal and vertical)
    #
    Filter.kernel = gaussianKernel(Filter.kernelSize, Filter.kernelSize)
    #################
    central = m.floor((Filter.kernelSize / 2))

    C = np.zeros((size.A.lin + central * 2, size.A.col + central * 2))
    C[(0 + central):(size.A.lin + central), (0 + central):(size.A.col + central)] = A

    #################
    ##  Run the kernel over the matrix (similar to convolution):
    #################
    soma = 0
    D = np.zeros(A.shape)

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):
            # Run kernel in one matrix's elements
            for kl in range(0, Filter.kernelSize):
                for kk in range(0, Filter.kernelSize):

                    soma = (C[j + kl, k + kk] * Filter.kernel[kl, kk]) + soma

            #value = m.ceil((soma / (Filter.kernelSize * Filter.kernelSize)))
            value = m.ceil((soma))
            soma = 0
            D[j, k] = value

    D = np.uint8(D)

    print('################################')
    print('Process finished')
    print('Filter have been applied')
    print('################################')

    return D

def gaussianKernel(h1, h2):

    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    import navFunc as nf

    ## Returns a normalized 2D gauss kernel array for convolutions

    x, y = np.mgrid[0:h2, 0:h1]
    x = x-h2/2
    y = y-h1/2
    sigma = 0.5
    g = np.exp( -( x**2 + y**2 ) / (2*sigma**2) )
    return g / g.sum()


'''
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
'''