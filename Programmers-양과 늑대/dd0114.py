import sys

s, c = map(int,input().split())
pa = []
total = 0

for i in range(s):
    a = int(sys.stdin.readline())
    pa.append(a)
    total += a

left = 0
right = max(pa)
save =0

while left <= right:
    sli =0
    mid = (left+right)//2
    if mid ==0:
        break

    for i in pa:
        sli += i//mid
    
    if sli >= c:
        left = mid+1
        
    else :#sli > c
        right =mid-1

total = total-(c*right)
print(total)