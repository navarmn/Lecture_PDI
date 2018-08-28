def eqHist (Image):
    ### Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    import navFunc as nf

    A = Image

    size = nf.structtype()
    size.A = nf.structtype()
    size.A.lin, size.A.col = A.shape

    #################### Equalize Histogram
    ## Pre-sets:

    newA = np.zeros((size.A.lin, size.A.col))

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):
            newA[j, k] = np.ceil(255*(
                         (A[j, k] - A.min()) /
                         (A.max() - A.min())))

    newImage = np.uint8(newA)

    print('################################')
    print('Process finished')
    print('Histogram has been equalized')
    print('################################')

    return newImage
