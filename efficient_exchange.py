from ecc import scalar_mult
from decrypt import decrypt_flag

a = 497 
b = 1768
p = 9739
param = (a, b, p)

q_x = 4726
nB = 6534

y_2 = q_x**3 + a*q_x + b
q_y = pow(y_2, (p+1)//4, p)
Q = (q_x, q_y)

shared_secret = scalar_mult(param, Q, nB)[0]
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))