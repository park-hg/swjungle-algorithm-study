max_value = 0

def dfs(s, graph, info, sh, wlf, odr_list):
    global max_value

    if sh == wlf:
        return

    max_value = max(max_value, sh)
    for idx in odr_list:
        temp = [num for num in odr_list if num != idx]
        if info[idx] == 0:
            dfs(idx, graph, info, sh + 1, wlf, temp + graph[idx])
        else:
            dfs(idx, graph, info, sh, wlf + 1, temp + graph[idx])

def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for s, d in edges:
        graph[s].append(d)

    dfs(0, graph, info, 1, 0, graph[0])
    
    return max_value
