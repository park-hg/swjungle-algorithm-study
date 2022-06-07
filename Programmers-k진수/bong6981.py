def is_prime(n):
    if n == 0:
        return False
    if n== 1 :
        return False
    
    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(n, k):
    num = []
    while n > 0:
      num.append(str(n%k))
      n = n//k
    
    num.reverse()
    
    ans = 0
    if '0' not in num:
        if is_prime(int("".join(num))):
            ans += 1
    else:
        nums = []
        start = 0
        end = 0
        while end < len(num):
            if end == len(num)-1 and num[end] != '0':
                nums.append(int("".join(num[start:end+1])))
            if num[end] == '0':
                if start != end and end != 0:
                    nums.append(int("".join(num[start:end])))
                start = end+1
            end += 1
        
        for n in nums:
            if is_prime(n):
                ans += 1
    return ans
                

