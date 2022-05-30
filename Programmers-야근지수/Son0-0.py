def solution(n, works):
    answer = 0
    size = len(works)
    
    while n != 0:
        max_value = max(works)
        for idx in range(size):
            if works[idx] == 0: continue
            if n == 0: break
            if max_value <= works[idx]:
                works[idx] -= 1
                n -= 1
        
        if sum(works) == 0:
            break
    
    for h in works:
        if 0 < h:
            answer += h ** 2
    
    return answer
