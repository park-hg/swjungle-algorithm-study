def solution(n, s):
    if (s // n) == 0: return [-1]
    num = s // n
    answer = [num for _ in range(n)]
    if (s % n) != 0:
        temp = (s % n)
        for idx in range(n):
            if temp == 0:
                break
            answer[idx] += 1
            temp -= 1
        return sorted(answer)
    else:
        return answer
