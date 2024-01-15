from hashlib import sha1
from ecc import scalar_mult

a = 497 
b = 1768
p = 9739
param = (a, b, p)

qA = (815, 3190)
nB = 1829

key = str(scalar_mult(param, qA, nB)[0])

m = sha1()
m.update(key.encode())
hash_digest = m.hexdigest()

print(f"flag : crypto{{{hash_digest}}}")