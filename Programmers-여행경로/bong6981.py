from collections import defaultdict, deque

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
                visited[i] = True
                ret = dfs(arr+[des])
                visited[i] = False
                if ret != []:
                    return ret
        
        return []
    
    # tickets.sort()
    # info = defaultdict(deque)

    # for i, t in enumerate(tickets):
    #     s = t[0]
    #     e = t[1]
    #     info[s].append(e)

    # def other(arr, start):

    #     while info[start]:
    #         des = info[start].popleft()
    #         other(arr, des)

    #     arr.append(start)
   
    
    dfs(["ICN"])
    return dfs(["ICN"])
    # arr = []
    # other(arr, "ICN")
    # return arr[::-1]
    
    

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
