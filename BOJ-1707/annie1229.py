# 15. 이분 그래프
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input())

def dfs(graph, idx, color):
    global visited, color_check

    visited[idx] = True
    new_color = "red"
    if color == "red":
        new_color = "black"
    check_color[idx] = new_color

    for node in graph[idx]:
        if not visited[node]:
            dfs(graph, node, new_color)

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    check_color = {}

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dfs(graph, 1, "red")
    
    flag = True
    for idx in range(1, len(graph)):
        for n in graph[idx]:
            if idx not in check_color:
                dfs(graph, idx, "red")
            if n not in check_color:
                dfs(graph, n, "red")
            if check_color[idx] == check_color[n]:
                flag = False
                break
                
    if flag:
        print("YES")
    else:
        print("NO")