import sys
from collections import deque

import pprint

N = int(sys.stdin.readline().strip())
time = {}
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
  for x, y in enumerate(map(int, sys.stdin.readline().split())):
    if x == 0:
      time[i] = y
    elif y == -1:
      break
    else:
      graph[y].append(i)
      in_degree[i] += 1

answer = [0] * (N + 1)
queue = deque()

for i in range(1, N + 1):
  if in_degree[i] == 0:
    queue.append(i)
    answer[i] = time[i]
    
while queue:
  curr = queue.popleft()
  
  for next in graph[curr]:
    in_degree[next] -= 1
    answer[next] = max(answer[next], answer[curr] + time[next])
    
    if in_degree[next] == 0:
      queue.append(next)

print(*answer[1:])
  
      
