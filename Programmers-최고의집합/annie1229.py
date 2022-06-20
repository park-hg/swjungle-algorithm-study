def solution(n, s):
    result = []
    divide = s // n
    left = s % n
    if divide < 1:
        return [-1]
    
    for nn in range(n):
        result.append(divide)
        
    if left:
        for l in range(left):
            result[l] += 1
    result.sort()
    return result
