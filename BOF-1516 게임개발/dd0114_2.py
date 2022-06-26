import sys
from collections import deque

answer = 0
n = int(input())

time = [0]*(n+1)
links = [[] for _ in range(n+1)] 
prev = [[] for _ in range(n+1)]
ind = [0]*(n+1)

q = deque([])

for i in range(1,n+1):

    tmp = list(map(int,sys.stdin.readline().split()))
    length = len(tmp)

    time[i] = tmp[0]
    ind[i] = length-2
    if length-2 == 0 :
        q.append(i)
    else :    
        for j in range(1,length-1):
            links[tmp[j]].append(i)
            prev[i].append(tmp[j])  



while q :
    now = q.popleft()
    tmp = 0 
    for i in prev[now]:
        tmp = max(tmp,time[i])
    time[now] += tmp
    
    for i in links[now]:
        ind[i] -= 1
        if ind[i] == 0:
            q.append(i)

for i in range(1,n+1):
    print(time[i])

    
