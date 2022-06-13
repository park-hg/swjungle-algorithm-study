from collections import defaultdict, deque

def solution(tickets):
    tickets.sort()
    info = defaultdict(deque)
    
    for i, t in enumerate(tickets):
        s = t[0]
        e = t[1]
        info[s].append(e)
    
    # def dfs(arr):
    #     if len(arr) == len(tickets) + 1:
    #         return arr
        
    #     start = arr[-1]
    #     des = info[start].popleft()
    #     return dfs(arr+[des])
    
    def other(arr, start):

        while info[start]:
            des = info[start].popleft()
            other(arr, des)
        
        arr.append(start)
        
    arr = []
    other(arr, "ICN")
    return arr[::-1]
    
    

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
