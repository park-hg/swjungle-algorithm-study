import sys
import math
sys.stdin = open('input.txt')

Q = int(sys.stdin.readline())

def get_num(n, x, y):
    p = min(x, y, n+1-x, n+1-y)
    s = 4*(p-1)*n - (p-1)**2

    if x == p:
        return s + 1 + (y-p)
    elif y == n+1-p:
        return s + (n-2*p) + (x-p)
    elif x == n+1-p:
        return s + 2*(n-2*p) + (y-p)
    elif y == p:
        return s + 3*(n-2*p) + (x-p)

def get_coordinate(n, z):
    p = int(2*n - math.sqrt(4*n**2-z) +1)
    s = z-p
    

for _ in range(Q):
    q = list(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        n, x, y = q[1:]
        print(get_num(n, x, y))
    else:
        n, z = q[1:]
        print(get_coordinate(n, z))