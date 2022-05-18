# boj-2617
# DFS

import sys

sys.setrecursionlimit(10 ** 7)

def dfs(graph, now, visited):
  global count, answer
  visited[now] = True
  
  if count == (N + 1) // 2: 
    return

  for next in graph[now]:
    if visited[next] == False:
      count += 1
      dfs(graph, next, visited)
  

N, M = map(int, sys.stdin.readline().split())
bigger = [[] for _ in range(N+1)]
smaller = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  bigger[a].append(b)
  smaller[b].append(a)

answer = [0] * (N + 1)
for b in range(1, N + 1):
  count = 0
  visited_b = [False] * (N + 1)
  dfs(bigger, b, visited_b)
  if count >= (N + 1) // 2: 
    answer[b] = 1

for s in range(1, N + 1):
  count = 0
  visited_s = [False] * (N + 1)
  dfs(smaller, s, visited_s)
  if count >= (N + 1) // 2:
    answer[s] = 1

print(answer.count(1))
