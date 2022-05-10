# 11. 사다리(#2022)
import sys
sys.stdin = open('input.txt')

x, y, c = map(float, sys.stdin.readline().split())

start = 0
end = min(x, y)
answer = 0

while start+0.0001 <= end:
    mid = (start + end) / 2
    h1 = (x**2 - mid**2)**0.5
    h2 = (y**2 - mid**2)**0.5
    res = (h1 * h2) / (h1 + h2)

    if res < c:
        end = mid
    else:
        start = mid
        answer = mid

print("{:.3f}".format(answer))