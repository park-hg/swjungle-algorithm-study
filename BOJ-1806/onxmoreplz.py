## 시간 초과


import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * N

flag = False
answer = 0
if sum(nums) < S:
  print(0)
else:
  while not flag:
    
    for i in range(N - answer):
      dp[i] += nums[i+answer]
      if dp[i] >= S:
        flag = True
        break
    # print(dp)
        
      
    answer += 1
  
  if flag:
    print(answer)
