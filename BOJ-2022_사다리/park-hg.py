import sys
import math
sys.stdin = open('input.txt')

x, y, c = map(float, sys.stdin.readline().split())
x *= 1000
y *= 1000
c *= 1000

def func(a):
    return c/math.sqrt(x**2-a**2) + c/math.sqrt(y**2-a**2)

left, right = 0, min(x, y)
while left < right:
    mid = (left + right) // 2
    if func(mid) < 1:
        left = mid+1
    else:
        right = mid

ans = (float(left)/1000)
print(ans)