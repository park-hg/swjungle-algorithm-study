import math

def solution(numbers):
    n = len(numbers)
    visited = [False]*n
    num_set = set()
    
    def backtrack(cur, depth):
        if depth == n+1:
            return
        
        if len(cur) > 0:
            num_set.add(int(cur))
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                backtrack(cur+numbers[i], depth+1)
                visited[i] = False
    
    backtrack('', 0)

    answer = 0
    for num in num_set:
        if num > 1:
            flag = True
            for b in range(2, int(math.sqrt(num))+1):
                if num%b == 0:
                    flag = False
                    break
            if flag:
                answer += 1
                
    return answer