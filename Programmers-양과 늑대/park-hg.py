from collections import defaultdict

def solution(info, edges):
    def dfs(state):
        nonlocal answer
        
        if visited[state]:
            return
        
        visited[state] = True
        
        wolf, sheep = 0, 0
        for i in range(n):
            if state & (1<<i):
                if info[i] == 0:
                    sheep += 1
                else:
                    wolf += 1
        
        if wolf >= sheep:
            return
        
        answer = max(answer, sheep)
        
        for v in range(n):
            if state & (1<<v):
                for w in graph[v]:
                    if not (state & (1<<w)):
                        dfs(state|(1<<w))
    
    n = len(info)
    graph = defaultdict(list)
    for i in range(len(edges)):
        a, b = edges[i]
        graph[a].append(b)

    visited = [False]*(1<<n)
    answer = 0
    
    dfs(1)
    return answer