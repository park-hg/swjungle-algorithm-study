
import sys

N, M = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))

if N <= M:
    print(N)
    exit(0)

def func(x):
    return sum([(x//t+1) for t in T])


left, right = 0, 6*10**10+1
while left < right:
    mid = (left+right) // 2
    if func(mid) < N:
        left = mid+1
    else:
        right = mid

print(left, mid, func(mid))
left_child = N-func(mid)

for i in range(M):
    if T[i]*(left//T[i]) > mid:
        left_child -= 1
    

l = [(T[i]*(left//T[i]), i+1) for i in range(M) if T[i]*(left//T[i]) <= mid]


l.sort()
print(l[left_child][1])

