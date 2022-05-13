import sys

sys.setrecursionlimit(10 ** 8)

def dfs(curr, side):
  group[curr] = side
  for next in graph[curr]:
    if group[next] == 0:
      if not dfs(next, -side):
        return False
    elif group[next] == side:
        return False
        
  return True
    
  
  
K = int(sys.stdin.readline().strip())
for _ in range(K):
  V, E = map(int, sys.stdin.readline().split())
  graph = [[] for _ in range(V + 1)]
  group = [0] * (V + 1)

  # 그래프 생성
  for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

  # DFS
  answer = "YES"
  for i in range(1, V + 1):
    if group[i] == 0:
      if not dfs(i, 1):
        answer = "NO"
        break
        
  print(answer)
