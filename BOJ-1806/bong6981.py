import sys
input = sys.stdin.readline


def sol():
    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))

    if sum(numbers) < s:
        return 0

    acc = [0]
    acc_v = 0
    for i in range(n):
        acc_v += numbers[i]
        acc.append(acc_v)

    ans = len(numbers)
    for i in range(1, n+1):
        start = i
        end = n
        tmp_ans = n
        while start <= end:
            mid = (start+end) // 2
            if acc[mid]- acc[i-1] >= s:
                tmp_ans = mid - i + 1
                end = mid -1
            else:
                start = mid + 1
        ans = min(ans, tmp_ans)
    return ans

print(sol())
