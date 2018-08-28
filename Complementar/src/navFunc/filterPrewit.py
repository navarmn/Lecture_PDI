def filterPrewit (Filter):
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

    #################### Prewit filter
    ## Pre-set steps:
    ### Generate two kernersl (horizontal and vertical)
    Filter.kernel = nf.structtype()
    Filter.kernel.horz = np.zeros((Filter.kernelSize, Filter.kernelSize))
    Filter.kernel.horz[:, 0] = -1
    Filter.kernel.horz[:, (Filter.kernelSize - 1)] = 1

    Filter.kernel.vert = np.zeros((Filter.kernelSize, Filter.kernelSize))
    Filter.kernel.vert[0, :] = -1
    Filter.kernel.vert[(Filter.kernelSize - 1), :] = 1

    #################
    central = m.floor((Filter.kernelSize / 2))

    C = np.zeros((size.A.lin + central * 2, size.A.col + central * 2))
    C[(0 + central):(size.A.lin + central), (0 + central):(size.A.col + central)] = A

    #################
    ##  Run the kernel over the matrix (similar to convolution):
    #################
    somaHorz = 0;
    somaVert = 0;
    D = np.zeros(A.shape)

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):
            # Run kernel in one matrix's elements
            for kl in range(0, Filter.kernelSize):
                for kk in range(0, Filter.kernelSize):

                    somaHorz = (C[j + kl, k + kk] * Filter.kernel.horz[kl, kk]) + somaHorz
                    somaVert = (C[j + kl, k + kk] * Filter.kernel.vert[kl, kk]) + somaVert

            Ph = m.ceil((somaHorz / (Filter.kernelSize ** 2)))
            Pv = m.ceil((somaVert / (Filter.kernelSize ** 2)))
            somaHorz = 0
            somaVert = 0
            D[j, k] = np.sqrt(Ph**2 + Pv**2)
            # print('LINE has finished')

    D = np.uint8(D)

    print('################################')
    print('Process finished')
    print('Filter have been applied')
    print('################################')

    return D
