def add_helper(param, P, Q):

    
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    
    x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
    if (x1 == x2) and (y1 == -y2):
        return (0, 0)

    a, b, p = param

    s =         ((y1 - y2)*pow(x1 - x2, -1, p)) % p         if P!=Q            else ((3*pow(x1, 2, p) + a)*pow(2*y1, -1, p)) % p
    x3 = (pow(s, 2, p) - x1 - x2) % p
    y3 = (s*(x1 - x3) - y1) % p
    return (x3, y3)

def add(param, *points):
    R = points[-1]
    for i in range(len(points)-2, -1, -1):
        R = add_helper(param, points[i], R)
    return R

def scalar_mult(param, Q, n):
    R = (0, 0)
    while n > 0:
        if n%2 == 1: 
            R = add(param, R, Q)
        Q = add(param, Q, Q)
        n = n//2
    return R

