def solution(n, cores) :
    
    c_len = len(cores)
    if n <= c_len :
        return n
    
    answer = 0
    time = 0
    left_value = 0
    right_value = cores[-1] * n
    
    while left_value <= right_value :
        
        mid_value = (left_value + right_value) // 2
        total = c_len
        
        for i in range(c_len) :
            total += mid_value // cores[i]
            
        if total < n :
            left_value = mid_value + 1          
        else:
            right_value = mid_value - 1
            time = mid_value
            
    cnt = c_len
    
    for i in range(c_len) :
        cnt += (time-1) // cores[i]

    for i in range(c_len) :
        if time % cores[i] == 0 :
            cnt += 1
            
            if cnt == n :
                answer = i + 1
                break
                     
    return answer