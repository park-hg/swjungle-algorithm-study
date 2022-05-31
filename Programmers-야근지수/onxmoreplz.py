def solution(n, works):
    if sum(works) <= n:
        answer = 0
    else:
        while n > 0:
            works.sort(reverse = True)
            max_value = max(works)
            for i in range(len(works)):
                if works[i] == max_value and n > 0:
                    works[i] -= 1
                    n -= 1
                else:
                    break
        answer = 0
        for i in range(len(works)):
            answer += works[i] ** 2
    
    
    return answer
