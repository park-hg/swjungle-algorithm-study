import sys
 a

S, C = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for _ in range(S)]

def func(x):
    ans = 0
    for i in l:
        ans += i//x
    
    return ans

left, right = -1, 10**10

while left < right:
    mid = (left+right) // 2
    if func(mid) >= C:
        left = mid + 1
    else:
        right = mid

ans = 0
for i in l:
    ans += i%(left-1)
print(ans)
