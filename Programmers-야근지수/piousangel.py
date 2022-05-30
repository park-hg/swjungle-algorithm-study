import heapq
import math

def solution(n, works):
    answer = 0
    heap = []
    total = 0
    
    for i in range(len(works)) :
        total += works[i]
        heapq.heappush(heap, (-works[i], works[i]))
        # heapq.heappush(heap, works[i])
        
    if total <= n : #피로없음
        return 0
    
    while n > 0 :
        temp = heapq.heappop(heap)[1]
        if temp == 0 : #큰 것부터 빼니까 
            break
        
        heapq.heappush(heap, (-temp + 1, temp - 1))
        n -= 1
    
    while len(heap) > 0 :
        tmp = heapq.heappop(heap)[1]
        answer += pow(tmp, 2)
        
    return answer