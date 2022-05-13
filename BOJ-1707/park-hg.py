import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

def bfs():
    visited = [0]*(V+1)

    for i in range(V+1):
        if visited[i] == 0:
            que = deque([[i, 1]])
            while que:
                v, color = que.popleft()
                for w in graph[v]:
                    if visited[w] == color:
                        print("NO")
                        return
                    if visited[w] == 0:
                        visited[w] = -color
                        que.append([w, -color])
    print("YES")
    return

K = int(sys.stdin.readline())
for _ in range(K):
    graph = defaultdict(list)
    V, E = map(int, sys.stdin.readline().split())
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    bfs()
