import math

# 각 원소의 합이 S
# 곱이 최대

def solution(n, s):
    answer = []
 
    total = 1
    
    
    if n > s :  # n이 s보다 크면 무조건 불가능
        return [-1]
    
    while n > 0 :
        
        temp = math.ceil(s/n)
        answer.append(temp)
        s -= temp
        n -= 1

    answer.sort()
    return answer