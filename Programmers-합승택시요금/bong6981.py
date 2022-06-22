def solution(n, s, a, b, fares):
    
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for p1, p2, cost in fares:
        graph[p1][p2] = cost 
        graph[p2][p1] = cost
        
    for k in range(1, n+1):
         for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
            
    
    ans = INF
    for i in range(1, n+1):
        c1 = graph[s][i]
        if c1 == INF:
            continue
        c2 = graph[i][a]
        if c2 == INF:
            continue
        c3 = graph[i][b]
        if c3 == INF:
            continue
        ans = min(ans, c1+c2+c3)
    
    return ans
    
    
    answer = 0
    return answer
