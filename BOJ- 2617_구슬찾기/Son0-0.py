import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 구슬의 개수 / 저울에 올려 본 쌍의 개수
graph_a = [[] for _ in range(N + 1)]
graph_b = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph_a[b].append(a)
  graph_b[a].append(b)

def dfs(v, graph, visited):
  for idx in graph[v]:
    if not idx in visited:
      visited.append(idx)
      dfs(idx, graph, visited)
  
  return visited
  
def solution():
  result = 0
  for idx in range(1, N + 1):
    result_a, result_b = dfs(idx, graph_a, []), dfs(idx, graph_b, [])
    if (N // 2) + 1 <= len(result_a):
      result += 1
    elif (N // 2) + 1 <= len(result_b):
      result += 1
  
  print(result)
  
solution()
