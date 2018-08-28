def multiLimiar (Filter):
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

    if Filter.multiLimiar.size == 2:
        T2 = Filter.multiLimiar[1]
        T1 = Filter.multiLimiar[0]
        Gmin = 0
        Gmed = 127
        Gmax = 255

    if Filter.multiLimiar.size == 3:
        T3 = Filter.multiLimiar[2]
        T2 = Filter.multiLimiar[1]
        T1 = Filter.multiLimiar[0]
        Gmin = 0
        Gmed1 = Filter.multiRange[0]
        Gmed2 = Filter.multiRange[1]
        Gmax = 255
    #################### Limiar


    D = np.zeros(A.shape)

    for j in range((0), size.A.lin):
        for k in range((0), size.A.col):
            if Filter.multiLimiar.size == 3:
                if A[j, k] > T3:
                    D[j, k] = Gmax
                elif A[j,k] <= T3 and A[j, k] > T2:
                    D[j, k] = Gmed2
                elif A[j, k] <= T2 and A[j, k] > T1:
                    D[j, k] = Gmed1
                elif A[j,k] <= T1:
                    D[j, k] = Gmin

            elif Filter.multiLimiar.size == 2:
                if A[j, k] > T2:
                    D[j, k] = Gmax
                elif A[j,k] <= T2 and A[j, k] > T1:
                    D[j, k] = Gmed
                elif A[j,k] <= T1:
                    D[j, k] = Gmin

    D = np.uint8(D)

    print('################################')
    print('Process finished')
    print('Multilimiar have been applied')
    print('################################')

    return D
