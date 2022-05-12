#형규형이 가르쳐주셨습니다. 감사합니다.
def dfs(status, graph, info, visited, n):
    global answer
    
    if visited[status] == True :
        return
    
    visited[status] = True
    
    wolf, lamb = 0, 0
    for i in range(n):
        if status & (1<<i):
            if info[i] == 0:
                lamb += 1
            else:
                wolf += 1
    
    if wolf >= lamb:
        return
    
    answer = max(answer, lamb)
            
    for i in range(n):
        if status & (1<<i):
            for j in graph[i]:
                if not (status & (1<<j)):
                    dfs(status|(1<<j), graph, info, visited, n)
                    
answer = 0

def solution(info, edges):
    global answer
    n = len(info)
    graph = [[] for _ in range(n)]
    visited = [0] * (1 << n)
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    dfs(1, graph, info, visited, n)
    
    return answer