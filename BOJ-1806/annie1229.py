# 26. 부분합(BOJ-1806)
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

result = sys.maxsize
sum_nums = deque()
sum_result = 0
end_idx = 0
for n in range(N):
    if sum_nums:
        pop = sum_nums.popleft()
        sum_result -= pop
    while sum_result < S and end_idx < N:
        add_num = nums[end_idx]
        sum_nums.append(add_num)
        sum_result += add_num
        end_idx += 1
    if sum_result >= S:
        result = min(result, len(sum_nums))
    # print(n, sum_nums, result)
if result == sys.maxsize:
    print(0)
else:
    print(result)