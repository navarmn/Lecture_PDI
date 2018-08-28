def filterLaplace (Filter):
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

    #################### Laplace filter
    ## Pre-set steps:
    Filter.kernel = np.ones((Filter.kernelSize, Filter.kernelSize))
    Filter.kernel[int(Filter.kernelSize/2), int(Filter.kernelSize/2)] = -1*(np.sum(Filter.kernel)-1)
    #################
    central = m.floor((Filter.kernelSize / 2))

    C = np.zeros((size.A.lin + central * 2, size.A.col + central * 2))
    C[(0 + central):(size.A.lin + central), (0 + central):(size.A.col + central)] = A

    #################
    ##  Run the kernel over the matrix (similar to convolution):
    #################
    soma = 0;
    D = np.zeros(A.shape)

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):
            # Run kernel in one matrix's elements
            for kl in range(0, Filter.kernelSize):
                for kk in range(0, Filter.kernelSize):
                    # print(C[j + kl, k + kk])
                    # print(kernel[kl, kk])
                    # print('Result is: %d ' %(C[j + kl,k + kk] * kernel[kl,kk]))

                    soma = (C[j + kl, k + kk] * Filter.kernel[kl, kk]) + soma

                    # print('Pixel has finished')
            value = m.ceil((soma / (Filter.kernelSize * Filter.kernelSize)))
            soma = 0
            D[j, k] = value
            # print('LINE has finished')

    D = np.uint8(D)

    print('################################')
    print('Process finished')
    print('Filter have been applied')
    print('################################')

    return D
