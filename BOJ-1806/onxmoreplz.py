## 재 도 전

import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


if sum(nums) < S:
  print(0)
else:
  lp, rp = 0, 0
  sums = 0
  answer = sys.maxsize
  while True:
    if sums >= S:
      answer = min(answer, rp - lp)
      sums -= nums[lp]
      lp += 1
    elif rp == N:
      break
    else:
      sums += nums[rp]
      rp += 1


  print(answer)
