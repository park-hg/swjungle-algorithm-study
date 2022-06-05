## 효율성 테스트 3개 실패 
import heapq

def solution(n, cores):
    if n <= len(cores):
        return n
    
    q = []
    for i, v in enumerate(cores):
        heapq.heappush(q, (v, i))

    t = 0    
    for i in range(len(cores)+1, n+1):
        complete_time, index = heapq.heappop(q)
        t = complete_time
        heapq.heappush(q, (t+cores[index], index))
        if i == n:
            return index+1

print(solution(6, [1,2,3]))
