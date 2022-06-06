def solution(n, cores):
    max_time = max(cores)*n

    l = 0
    r = max_time

    while l <= r:
        mid = (l+r)//2
        work = 0
        for core in cores:
            work += (mid // core)+1
        
        if work >= n:
            r = mid-1
        else :
            l = mid+1

    
    prev_time = l-1
    prev_work = 0
    for j in cores:
        prev_work += (prev_time //j) +1

    n -= prev_work
    for i in range(len(cores)):
        core = cores[i]
        if l%core == 0:
            n -= 1
            if n == 0:
                return i+1  

n = 6
cores =	[1,2,3]	
print(solution(n,cores))