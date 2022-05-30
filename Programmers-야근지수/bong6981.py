def solution(n, works):
    
    ## n만큼 일할 수 있는데, works에서 n만큼 빼서, 그 제곱을 더한 값이 최소가 되도록 한다. 
    
    left = n
    works.sort(reverse=True)
    
    while True:
        if left == 0:
            break
        max_v = works[0]
        if max_v == 0:
            break
        for i in range(len(works)):
            if left == 0:
                break
            if works[i] == max_v:
                works[i] -= 1
                left -= 1
            else:
                break
        
    answer = 0
    for i in works:
        answer += i ** 2
    
    return answer
