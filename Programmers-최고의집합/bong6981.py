from collections import deque

def solution(n, s):
    
    m, l = divmod(s, n)
    
    if m == 0:
        return [-1]
    ans = [m] * n
    if l == 0:
        return ans 
    
    idx = len(ans) -1 
    for _ in range(l):
        ans[idx] += 1
        idx -= 1
    return ans
    
        
        
        
        
    
        
