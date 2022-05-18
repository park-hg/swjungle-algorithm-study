import sys
from collections import deque
sys.stdin = open('sample.txt')
open = sys.stdin.readline

n, m = map(int, input().split()) #구슬, 밑에 몇줄?

bigger_graph = [[] for _ in range(n+1)]
smaller_graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    smaller_graph[a].append(b)
    bigger_graph[b].append(a)

# print("bigger_graph", bigger_graph)
# print("smaller_graph", smaller_graph)

def chk(graph, visited, idx) :
    temp  = 0
    visited[idx] = True
    q = deque()
    q.append(idx)

    while q :
        now_idx = q.popleft()
        
        for node in graph[now_idx] :
            if visited[node] != True :
                visited[node] = True
                q.append(node)
                temp += 1
    # print("temp", temp)
    return temp

temp_list = []
answer = 0

for i in range(1, n+1):
    visited = [False] * (n+1)
    temp_list = [ chk(bigger_graph, visited, i), chk(smaller_graph, visited, i) ]
    if (n+1)//2 <= temp_list[0] or (n+1)//2 <= temp_list[1] :
        answer += 1

print(answer)


