from ecc import scalar_mult

a = 497 
b = 1768
p = 9739
param = (a, b, p)

X = (5323, 5438)
print(scalar_mult(param, X, 1337) == ((1089, 6931)))

P = (2339, 2213)
Q = scalar_mult(param, P, 7863)

print(f"flag : crypto{{{Q[0]},{Q[1]}}}")