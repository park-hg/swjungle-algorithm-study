from itertools import permutations

def solution(numbers):
    answer = 0
    nums = list(numbers)
    nums.sort(reverse=True)
    max_num = int(''.join(nums))
    perm_nums = set()

    for length in range(1, len(nums) + 1):
        temp = permutations(nums, length)
        for t in temp:
            perm_nums.add(int(''.join(t)))

    primes = set([2])
    check_prime = [False, False, True] + [False for _ in range(max_num)]

    for n in range(3, max_num + 1):
        if n % 2 and not check_prime[n]:
            primes.add(n)
            for nn in range(n, max_num + 1, n):
                check_prime[nn] = True

    perm_nums = list(set(perm_nums))
    for num in perm_nums:
        if num in primes:
            answer += 1
    return answer