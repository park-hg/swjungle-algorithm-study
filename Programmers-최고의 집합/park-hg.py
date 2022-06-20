def solution(n, s):
    q, r = divmod(s, n)
    if q < 1:
        return [-1]
    answer = [q]*n
    for i in range(r):
        answer[-1-i] += 1
    return answer