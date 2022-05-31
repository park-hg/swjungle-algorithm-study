# 개표(BOJ-24913)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, Q = map(int, input().split())

result = [0 for _ in range(N + 2)]

for _ in range(Q):
  idx, num1, num2 = map(int, input().split())

  if idx == 1:
    result[num2] += num1
  elif idx == 2:
    mine = result[-1] + num1
    other_sum = round((sum(result[1:N+1]) + num2) / N)
    if(max(result[1:N+1]) < mine and other_sum < mine):
      print('YES')
    else:
      print('NO')
