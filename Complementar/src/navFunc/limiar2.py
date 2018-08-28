def limiar2 (Filter):
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

    #################### Limiar
    Tmin = np.min(A)
    Tmax = np.max(A)
    D = np.zeros(A.shape)

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):

            if A[j,k] < Filter.limiar:
                D[j, k] = Tmin
            else:
                D[j, k] = Tmax

    D = np.uint8(D)

    print('################################')
    print('Process finished')
    print('Limiar has been applied')
    print('################################')

    return D
