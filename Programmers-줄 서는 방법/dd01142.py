import math
answer = []
check = []

def sol(n,k,t,cnt):
    for i in range(1,n+1):
        if (i-1)*t < k <= i*t:
            ind = check.pop(i-1)
            answer.append(ind)
            cnt -= 1
            k -= (i-1)*t
            if cnt == 0:
                return
            sol(n,k,t/cnt,cnt)            
            return 

def solution(n, k):
    tmp = math.factorial(n)/n
    
    for i in range(n):
        check.append(i+1)
    
    sol(n,k,tmp,n)
    return answer

print(solution(3,5))