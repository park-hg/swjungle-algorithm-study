from collections import deque

# [A,B] A가 B한테 이겼다

def chk(start, graph, visited) :
    
    q = deque()
    q.append(start)
    visited[start] = True
    temp = 0
    while q :
        
        now = q.popleft()
        temp = max(temp, temp)
        for node in graph[now] :
            if visited[node] != True :
                visited[node] = True
                q.append(node)
                temp += 1
    # print(start, temp)
    return temp

def solution(n, results):
    answer = 0
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    
    for node in results :
        win_graph[node[0]].append(node[1])
        lose_graph[node[1]].append(node[0])
    
    # print(win_graph)
    # print(lose_graph)
    for i in range(1, n+1) :
        visited = [False] * (n+1)
        chk_temp = chk(i, win_graph, visited) + chk(i, lose_graph, visited)
        if chk_temp == n -1 :
            answer += 1
        
    return answer