def calcHist (Image):
    ### Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    import navFunc as nf

    # Load image into numpy matrix

    A = Image

    size = nf.structtype()
    size.A = nf.structtype()
    size.A.lin, size.A.col = A.shape

    #################### Calculate Histogram
    ## Pre-setes:
    if A.dtype == 'uint8':
        #buffer = np.linspace(0, 255, num = 2**8)
        #buffer = np.zeros((A.max()+1) - (A.min()))
        buffer = np.zeros((256))

    ## Read the intire matrix element-by-element:

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):

            buffer[(A[j, k])] += 1


    print('################################')
    print('Process finished')
    print('Histogram has been calculated')
    print('################################')

    return buffer
