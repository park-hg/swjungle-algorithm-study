from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    for target in range(2, num):
        if (num % target) == 0:
            return False
        
    return True

def solution(numbers):
    llist = []
    for i in range(1, len(numbers) + 1):
        llist += list(permutations(numbers, i))
    llist = list(set(llist))

    answer = []
    for num in llist:
        pnum = int(''.join(num))
        if isPrime(pnum) == True:
            answer.append(pnum)
            
    answer = list(set(answer))
    
    return len(answer)
