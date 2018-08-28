def filterMedian (Filter):
    ### Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    import navFunc as nf

    import time

    # Load image into numpy matrix

    A = Filter.img

    size = nf.structtype()
    size.A = nf.structtype()
    size.A.lin, size.A.col = A.shape

    #################### Mean filter
    ## Pre-set steps:
    Filter.kernel = np.ones((Filter.kernelSize, Filter.kernelSize))
    #################
    central = m.floor((Filter.kernelSize / 2))

    C = np.zeros((size.A.lin + central * 2, size.A.col + central * 2))
    C[(0 + central):(size.A.lin + central), (0 + central):(size.A.col + central)] = A

    #################
    ##  Run the kernel over the matrix (similar to convolution):
    #################
    buffer = np.zeros((Filter.kernelSize * Filter.kernelSize))
    D = np.zeros(A.shape)

    # for each line:
    for j in range((0), size.A.lin):
        # for each collumn:
        for k in range((0), size.A.col):
            # Run kernel in one matrix's elements
            ## for each line:
            for kl in range(0, Filter.kernelSize):
                ## for each collumn:
                for kk in range(0, Filter.kernelSize):

                    buffer[(Filter.kernelSize * kl + kk)] = (C[j + kl, k + kk])

            buffer = np.sort(buffer)
            value = buffer[int(np.floor((Filter.kernelSize**2)/2))]

            D[j, k] = value
            # print('LINE has finished')

    D = np.uint8(D)

    print('################################')
    print('Process finished')
    print('Filter have been applied')
    print('################################')

    return D
