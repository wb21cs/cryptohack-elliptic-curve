from ecc import add

a = 497 
b = 1768
p = 9739
param = (a, b, p)

X = (5274, 2841)
Y = (8669, 740)

print(add(param, X, X) == (7284, 2107))
print(add(param, X, Y) == (1024, 4440))

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)
S = add(param, P, P, Q, R)

print(f"flag : crypto{{{S[0]},{S[1]}}}")