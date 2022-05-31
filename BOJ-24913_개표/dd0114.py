import sys
import math

n, q = map(int,sys.stdin.readline().split())
now = [0]*(n+1)
me_pyo = 0

high = 0
total = 0

for i in range(q):
    a, b, c = map(int,sys.stdin.readline().split())

    if a == 1:
        if c == n+1:
            me_pyo += b
        else :
            now[c] += b
            total += b
            high = max(high,now[c])

    else :
        win = me_pyo + b
        
        if high >= win:
            print("NO")
        else :
            lose = math.ceil((total + c)/n)
            if win > lose:
                print("YES")
            else :
                print("NO")