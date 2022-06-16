import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)

def solution(tickets):
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)
        graph[src].sort(reverse=True)
    
    answer = []
    def dfs(cur):
        while graph[cur]:
            dfs(graph[cur].pop())
        answer.append(cur)
        
    dfs("ICN")
    
    return answer[::-1]
