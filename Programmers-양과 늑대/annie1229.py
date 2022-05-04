result = 0

def solution(info, edges):
    global result
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    result = 0
    
    def dfs(cur, sheep_cnt, wolf_cnt, next):
        global result
        if info[cur] == 0:
            sheep_cnt += 1
        else:
            wolf_cnt += 1
        if sheep_cnt > result:
            result = sheep_cnt
        if wolf_cnt >= sheep_cnt:
            return
        for idx, n in enumerate(next):
            dfs(n, sheep_cnt, wolf_cnt, next[:idx] + next[idx+1:] + graph[n])
        
    dfs(0, 0, 0, graph[0])
    
    return result
