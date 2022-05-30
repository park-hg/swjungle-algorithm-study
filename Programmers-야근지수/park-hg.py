def solution(n, works):
    n = min(sum(works), n)
    
    works.sort(reverse=True)
    
    while n:
        max_w = max(works)
        for i in range(len(works)):
            if works[i] == max_w:
                works[i] -= 1
                n -= 1
                if n == 0:
                    break
            else:
                break
    
    answer = 0
    for w in works:
        answer += w**2
    return answer