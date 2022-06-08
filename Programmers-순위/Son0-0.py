def solution(n, results):
    win_graph = [[] for _ in range(n + 1)]
    lose_graph = [[] for _ in range(n + 1)]
    
    for w, l in results:
        win_graph[w].append(l)
        lose_graph[l].append(w)
    
    def dfs(v, graph, visited = []):
        for idx in graph[v]:
            if idx not in visited:
                visited.append(idx)
                dfs(idx, graph, visited)
        
        return visited
    
    answer = 0
    for idx in range(1, n + 1):
        result_win, result_lose = dfs(idx, win_graph, []), dfs(idx, lose_graph, [])
        if (len(result_win) + len(result_lose)) == n - 1:
            answer += 1
    
    return answer
