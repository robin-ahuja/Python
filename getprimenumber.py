from math import sqrt
from pprint import pprint as pp

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x%i == 0:
            return False
    return True


def printprime():
    pp([x for x in range(101) if is_prime(x)])
    pp ('prime square division')
    pp({x*x:(1,x,x*x) for x in range(101) if is_prime(x)})

if __name__ == '__main__':
    printprime()