# Analyse Numérique
# TP mise à niveau
# Lilian Hiault

import numpy as np
import numpy.linalg as lg
import scipy.linalg as slg

L = [np.array([[1, 1], [0, 2]]),
     np.array([[1, 1], [0, 2]]),
     np.array([[1, 0], [1, 2]]),
     np.array([[1, 1], [0, 1]]),
     np.array([[1, 1], [1, 0]]),
     np.array([[1, 1], [1, 0]]),
     np.array([[1, 2], [2, 4]]),
     np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
     np.array([[11, -5, 5], [-5, 3, -3], [5, -3, 3]])]

for A in L:
    print("Matrice A:\n", A)

    E = lg.eig(A)
    print("E:\n", E)
    print("Valeurs propres :")
    for valp in E[0]:
        print(valp)
    print("Vecteurs propres :")
    for i in range(len(E[0])):
        print(E[1][:, i])

    D = np.diag(E[0])
    print("Diagonalisation:\n", D)
    

