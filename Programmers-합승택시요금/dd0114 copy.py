from cmath import inf
import heapq

def solution(n, s, a, b, fares):
    infi = 20000000
    box = [[infi]*(n+1) for _ in range(n+1)]
    answer = infi

    for i in fares:
        d1, d2, cost = i
        box[d1][d2] = cost
        box[d2][d1] = cost

    q = [] 

    for i in range(1,n+1):
        box[i][i] = 0

        if box[a][i] != infi:
            heapq.heappush(q, (box[a][i],i,a))
        if box[b][i] != infi:
            heapq.heappush(q, (box[b][i],i,b))
        if box[s][i] != infi:
            heapq.heappush(q, (box[s][i],i,s))
    
    while q:
        c, now, d = heapq.heappop(q)
        if now == d:
            continue

        for i in range(n+1):
            if c+box[now][i] < box[d][i]:
                box[d][i] = c+box[now][i]
                box[i][d] = c+box[now][i]
                heapq.heappush(q, (box[d][i],i,d))

    for i in range(1,n+1):
        answer = min(answer,box[s][i]+box[i][a]+box[i][b])

    return answer

n = 6
s = 4	
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# n = 6
# s = 4
# a = 5
# b = 6

# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(n,s,a,b,fares))
