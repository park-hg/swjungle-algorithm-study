from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    total = 0
    for a, b in tickets:
        graph[a].append(b)
        total += 1
    for a in graph:
        graph[a].sort()

    answer = []
    def dfs(v, discovered=["ICN"]):
        nonlocal answer, total
        if total == 0:
            answer.append(discovered)
            return
        
        for w in graph[v]:
            graph[v].remove(w)
            total -= 1
            dfs(w, discovered+[w])
            graph[v].append(w)
            graph[v].sort()
            total += 1
                
    dfs("ICN")
    answer.sort()

    return answer[0]