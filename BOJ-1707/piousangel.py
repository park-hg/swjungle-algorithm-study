import sys
from collections import deque
# sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

def dfs(v, color):

    visited[v] = color

    for i in graph[v] :
        if visited[i] == 0 :
            if not dfs(i, -color) :
                return False
        elif visited[i] == visited[v]:
            return False
    return True


for i in range(n):

    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for j in range(e) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    chkGraph = True

    for j in range(1, v+1) :
        if visited[j] == 0 :
          chkGraph = dfs(j, 1)
          if chkGraph == False:
              break
    
    if chkGraph :
        print("YES")
    else:
        print("NO")
