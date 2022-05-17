# 죄송합니다

import sys

input = sys.stdin.readline

N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

def dfs(idx, cnt):  
  if N <= idx:
    # print("end")
    return 
  
  global max_value
  max_value = max(max_value, cnt)
  # print(egg)
  
  # 내구도 / 무게 
  if 0 < egg[idx][0]:
    for i in range(idx + 1, N):
      if 0 < egg[i][0]:
        # CASE 1: 손에 들고 있는 계란 깨졌을 때
        if (egg[idx][0] - egg[i][1]) <= 0 and 0 < (egg[i][0] - egg[idx][1]):
          egg[idx][0] -= egg[i][1]
          egg[i][0] -= egg[idx][1]
          dfs(idx + 1, cnt + 1)
          egg[i][0] += egg[idx][1]
          egg[idx][0] += egg[i][1]
        # CASE 2: 친 계란이 깨졌을 때
        elif (egg[i][0] - egg[idx][1]) <= 0 and 0 < (egg[idx][0] - egg[i][1]):  
          egg[i][0] -= egg[idx][1]
          egg[idx][0] -= egg[i][1]
          dfs(idx, cnt)
          egg[idx][0] += egg[i][1]
          egg[i][0] += egg[idx][1]
        # CASE 3: 둘 다 깨졌을 때
        elif (egg[i][0] - egg[idx][1]) <= 0 and (egg[idx][0] - egg[i][1]) <= 0:
          egg[idx][0] -= egg[i][1]
          egg[i][0] -= egg[idx][1]
          dfs(idx + 1, cnt + 2)
          egg[idx][0] += egg[i][1]
          egg[i][0] += egg[idx][1]
        # CASE 4: 둘 다 안깨졌을 때
        else:
          egg[idx][0] -= egg[i][1]
          egg[i][0] -= egg[idx][1]
          dfs(idx, cnt)
          egg[idx][0] += egg[i][1]
          egg[i][0] += egg[idx][1]
  else:
    dfs(idx + 1, cnt)
        

def solution():
  dfs(0, 0)
  print(max_value)

solution()
