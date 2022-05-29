def real_search(graph, i, caller):
    cnt = 0
    for des in graph[i]:
        if des != caller:
            cnt += 1
            cnt += real_search(graph, des, i)
    return cnt
    
def search(graph, i, j):
    return abs(real_search(graph, i, j) - real_search(graph, j, i))
    
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    answer = 200
    for node1, node in wires:
        answer = min(answer, search(graph, node1, node))
        
    return answer


