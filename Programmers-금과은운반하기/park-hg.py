def solution(a, b, g, s, w, t):
    n = len(g)
    def func(x):
        max_gold, max_silver, max_weight = 0, 0, 0
        for i in range(n):
            cnt = (x//t[i]+1)//2
            max_weight += (x//t[i]+1)//2 * w[i]
            max_gold += min(g[i], max_weight)
            max_silver += min(s[i], max_weight)
        
        return max_gold, max_silver, max_weight
    
    left, right = 0, 4*10**14+1
    while left < right:
        mid = (left+right) // 2
        mid_gold, mid_silver, mid_weight = func(mid)
        # print(mid, func(mid))
        if mid_gold < a or mid_silver < b or mid_weight < a+b:
            left = mid+1
        else:
            right = mid-1
    
    return left