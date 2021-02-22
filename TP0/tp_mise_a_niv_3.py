# Analyse Numérique
# TP mise à niveau
# Lilian Hiault

import numpy as np
import numpy.linalg as lg

M = np.array([[0.4, 0.3],
              [0.9, 0.7]])
d = np.array([[0.3],
              [0.7]])
x = lg.solve(M, d)
print(f"Solution x : {x}")

d1 = np.array([[0.31],
               [0.7]])
x1 = lg.solve(M, d1)
print(f"Solution x1 : {x}")

condM = lg.cond(M)
print(f"Conditionnement de M : {condM}")

deltad = lg.norm(d1 - d) / lg.norm(d)
print(f"Erreur d : {deltad}")
deltax = lg.norm(x1 - x) / lg.norm(x)
print(f"Erreur x : {deltax}")
ampli = deltax/deltad
print(f"Factteur d'amplification : {ampli}")
print(f"Facteur d'amplification de l'erreur par rapport au conditionnement : {erreur / condM * 100}")
