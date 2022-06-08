import sys

n,s,m = map(int,sys.stdin.readline().split())
v = list(map(int,sys.stdin.readline().split()))

d_check = (1<<(m+1))-1
new_check = n<<(s)
dummy = 1<<s
breaker = 0

for i in range(n):
    
    buf1 = d_check & (dummy << v[i])
    buf2 = d_check & (dummy >> v[i])
    dummy = buf1|buf2
    
    if dummy == 0:
        breaker = 1
        break

if breaker == 1:
    print(-1)
else :
    for i in range(m,-1,-1):
        if dummy & 1<<i == 1<<i:
            print(i)
            break