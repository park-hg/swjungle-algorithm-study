def solution(n, k):
    fac = [1]
    temp = 1
    for i in range(1,n+1):
        temp *= i
        fac.append(temp)
    
    nums = list(range(1, n+1))
    
    answer = []
    while k:
        q, k = divmod(k, fac[n-1])
        if k == 0:
            answer.append(nums[q-1])
            nums.remove(nums[q-1])
            nums.sort(reverse=True)
            answer += nums
            break
        else:
            answer.append(nums[q])
            nums.remove(nums[q])
            n -= 1
    
    return answer