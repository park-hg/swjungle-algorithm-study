def is_prime(num):
    cnt = 0

    if num == 1:
        return False
    target = int(num ** 0.5)
    for i in range(2, target + 1):
        if (num % i) == 0:
            cnt += 1
        if 0 < cnt:
            return False
    return True


def calc(num, k):
    answer = ''
    while 0 < num:
        answer += str(num % k)
        num //= k

    return answer[::-1]


def solution(n, k):
    answer = 0
    if k == 10:
        n = str(n)
    else:
        n = str(calc(n, k))
    num_list = [num for num in list(map(str, n.split('0'))) if num != '']

    for num in num_list:
        if is_prime(int(num)) == True:
            answer += 1

    return answer
