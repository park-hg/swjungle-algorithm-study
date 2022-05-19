import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

ind = [0]*(n+1)
links = [[]for _ in range(n+1)]

for _ in range(m):
    sc = list(map(int,sys.stdin.readline().split()))
    for i in range(1,sc[0]):
        links[sc[i]].append(sc[i+1])
        ind[sc[i+1]] += 1

q = deque([])
for i in range(1,n+1):
    if ind[i] == 0 :
        q.append(i)

ans = []

while q :
    a = q.popleft()
    ans.append(a)
    for j in links[a]:
        ind[j] -= 1
        if ind[j] == 0:
            q.append(j)

if len(ans) == n :
    for i in ans:
        print(i)
else :
    print(0)