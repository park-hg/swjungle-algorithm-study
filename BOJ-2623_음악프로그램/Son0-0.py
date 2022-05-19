import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
    llist = list(map(int, input().split()))
    for idx in range(1, len(llist) - 1):
        graph[llist[idx]].append(llist[idx + 1])
        indegree[llist[idx + 1]] += 1
        
print(graph)
print(indegree)


def topology_sort(result=[]):
    q = deque()

    for idx in range(1, N + 1):
        if indegree[idx] == 0:
            q.append(idx)

    while q:
        cur = q.popleft()
        result.append(cur)
        for idx in graph[cur]:
            indegree[idx] -= 1
            if indegree[idx] == 0:
                q.append(idx)

    return result


def solution():
    result = topology_sort()
    print(*result, sep='\n') if result else print(0)


solution()
