# Analyse numérique
# Lilian HIAULT
# TP 1 - Exercice 2 : Suite de Fibonnaci

from time import time
from math import sqrt

def fibo_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

def fibo_iter(n):
    cur = 1
    pre = 1
    for i in range(n-1):
        sum = cur + pre
        pre = cur
        cur = sum
    return cur

n = 20
start = time()
res = fibo_rec(n)
end = time()
print(f"fibo_rec({n}) = {res} en { end - start} secondes")

start = time()
res = fibo_iter(n)
end = time()
print(f"fibo_iter({n}) = {res} en { end - start} secondes")

def convergence(eps = 0.0001, arret = 10_000):
    i = 1
    diff = abs( (1+sqrt(5)) / 2) - (fibo_iter(i) / fibo_iter(i-1))
    while diff > eps and i < arret:
        diff = abs( (1+sqrt(5)) / 2) - (fibo_iter(i) / fibo_iter(i-1))
        i += 1
    if i < arret:
        print(f"Convergence à {i} itérations")
    else:
        print("Pas de convergence")

convergence()
