# ref: https://deep-learning-study.tistory.com/581

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
size = int(input())


def dfs(start, visited, color, graph):
    visited[start] = color

    for node in graph[start]:
        if visited[node] == 0:
            if not dfs(node, visited, -color, graph):
                return False
        elif visited[node] == visited[start]:
            return False

    return True


def solution():
    for _ in range(size):
        node, edge = map(int, input().split())
        graph = [[] for _ in range(node + 1)]
        visited = [0 for _ in range(node + 1)]
        for _ in range(edge):
            n, target = map(int, input().split())
            graph[n].append(target)
            graph[target].append(n)

        bipartite = True

        for idx in range(1, node + 1):
            if visited[idx] == 0:
                bipartite = dfs(idx, visited, 1, graph)
                if not bipartite:
                    break
        if bipartite:
            print("YES")
        else:
            print("NO")


solution()
