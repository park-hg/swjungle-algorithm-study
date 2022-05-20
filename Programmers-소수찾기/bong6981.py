def is_prime(num):
    if num == 0 or num == 1 :
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
def search(digit, numbers, depth, checked):
    if depth == digit:
        num = int("".join(numbers[:depth]))
        if num in checked:
            return 0
            
        checked.add(num)
        if is_prime(num):
            return 1
        return 0
    
    cnt = 0
    for i in range(depth, len(numbers)):
        numbers[depth], numbers[i] = numbers[i], numbers[depth]
        cnt += search(digit, numbers, depth+1, checked)
        numbers[depth], numbers[i] = numbers[i], numbers[depth]

    return cnt 
        
def solution(numbers):
    answer = 0
    checked = set()
    for i in range(1, len(numbers)+1):
        answer += search(i, list(numbers), 0, checked)
    return answer


# print(solution("17"))
# print(solution("011"))
