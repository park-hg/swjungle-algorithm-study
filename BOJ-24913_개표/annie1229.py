# 개표(BOJ-24913)
import sys
from math import ceil
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, Q = map(int, input().split())

result = [0 for _ in range(N + 2)]
total = 0
max_count = 0

for _ in range(Q):
  idx, num1, num2 = map(int, input().split())

  if idx == 1:
    result[num2] += num1
    if num2 <= N:
      total += num1
      max_count = max(max_count, result[num2])
  elif idx == 2:
    mine = result[-1] + num1
    other_sum = ceil((total + num2) / N)
    if(max_count < mine and other_sum < mine):
      print('YES')
    else:
      print('NO')
