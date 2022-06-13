from collections import defaultdict, deque
from pickle import TRUE


def solution(tickets):
    tickets.sort()
    info = defaultdict(deque)
    
    for i, t in enumerate(tickets):
        s = t[0]
        e = t[1]
        info[s].append(i)
    
    visited = [0] * len(tickets)
    def dfs(arr):
        if len(arr) == len(tickets) + 1:
            return arr
        
        start = arr[-1]
        for i in info[start]:
            if not visited[i]:
                des = tickets[i][1]
                visited[i] = TRUE
                ret = dfs(arr+[des])
                visited[i] = False
                if ret != []:
                    return ret
        
        return []
    
    dfs(["ICN"])
    return dfs(["ICN"])
    # arr = []
    # other(arr, "ICN")
    # return arr[::-1]
    
    

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
