import numpy as np

def fib_list(x, y, n):

    L = [x, y]

    for i in range(n-1):
        L.append(L[-1] + L[-2])

    return L[-1]


def fib_rec(x, y, n):
    
    z = x + y

    if n > 0:

        return fib_rec(y, z, n-1)

    else:

        return x


def fib_for(x, y, n):

    for i in range(n-1):
        z = x + y
        x = y
        y = z

    return z


def fib_cal(n):
    
    return int( ((1+np.sqrt(5))/2)**n/np.sqrt(5) + .5)
