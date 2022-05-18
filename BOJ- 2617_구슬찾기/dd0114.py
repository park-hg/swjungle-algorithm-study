import sys

n, m = map(int,sys.stdin.readline().split())

heavy = [[]for _ in range(n+1)]
light = [[]for _ in range(n+1)]
h_ind = [0]*(n+1)
l_ind = [0]*(n+1)

for i in range(m):
    h, l = map(int,sys.stdin.readline().split())
    heavy[l].append(h)
    h_ind[l] +=1
    
    light[h].append(l)
    l_ind[h] +=1

count = 0

def dfs_h(n):
    global count
    for i in heavy[n]:
        if visit[i] == True:
            visit[i] = False
            count += 1
            dfs_h(i)

def dfs_l(n):
    global count
    for i in light[n]:
        if visit[i] == True:
            visit[i] = False
            count += 1
            dfs_l(i)

ans = 0

for i in range(1,n+1):
    count = 0
    visit = [True]*(n+1)
    dfs_h(i)
    if count >= (n - n//2):
        ans += 1
        continue
    
    visit = [True]*(n+1)
    count = 0
    dfs_l(i)
    if count >= (n - n//2):
        ans += 1


print(ans)
