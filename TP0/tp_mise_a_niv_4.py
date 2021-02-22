# Analyse Numérique
# TP mise à niveau
# Lilian Hiault

import numpy as np
from math import factorial
import numpy.linalg as lg

def create_hilbert(n):
    H = np.reshape( np.array([1 / (i + j - 1) for i in range(1, n+1) for j in range(1, n+1)]), (n, n))
    return H

def det_hilbert(n):
    H = create_hilbert(n)
    det = 1
    kfact = 1
    nkfact = factorial(n)
    for k in range(0, n):
        if k != 0:
            kfact *= k
            nkfact *= n + k
        det *= kfact ** 3 / nkfact
    return det

print(create_hilbert(3))
print(f"Déterminant exact : {det_hilbert(11)}\nDéterminant lg : {lg.det(create_hilbert(11))}")

A = create_hilbert(5)
print(f"Hilbert d'ordre 5 :\n{A}\nSon inverse est :\n{lg.inv(A)}")

A1 = np.copy(A)
A1[0][0] = 999/1000
print(f"Hilbert d'ordre 5 modif :\n{A1}\nSon inverse est :\n{lg.inv(A1)}")
