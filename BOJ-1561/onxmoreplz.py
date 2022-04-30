## [2번] (백준 1561번) 놀이 공원

import sys

N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

if N <= len(times):
  print(N)
else:
  left = times[0]
  right = max(times) * N
  while left <= right:
    mid = (left + right) // 2
    non_passed = N - M
    for time in times:
      non_passed -= mid // time
      if non_passed <= 0:
        result_time = mid
        right = mid - 1
        break
    if non_passed > 0:
        left = mid + 1

  finished = M
  for i in range(len(times)):
    finished += (result_time - 1) // times[i]

  remain = [result_time % times[i] for i in range(M)]

  flag = False
  for i in range(len(remain)):
    if remain[i] == 0:
      finished += 1
    if finished == N:
      answer = i + 1
      flag = True
      break

  if flag:
    print(answer)
  else:
    print(M)
  
