import pprint

def solution(land):
  global answer
  answer = 0

  dp = [[0] * (4)] + land
  
  for i in range(1, len(land) + 1):      
    for j in range(4):
      dp[i][j] = dp[i][j] + max(
        dp[i-1][(j-1)%4],
        dp[i-1][(j-2)%4],
        dp[i-1][(j-3)%4]
      )

  # pprint.pprint(dp)
  answer = max(dp[len(land)])

  

  return answer
