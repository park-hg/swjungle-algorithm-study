import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    answer = sys.maxsize

    left, right = 0, 0
    num = nums[left]
    while left <= right and right < N:
        if num < S:
            if right == N - 1:
                break
            right += 1
            num += nums[right]
        else:
            answer = min(answer, right - left + 1)
            num -= nums[left]
            left += 1

    print(0) if answer == sys.maxsize else print(answer)

solution()
