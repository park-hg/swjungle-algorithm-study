from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)

whos_boss = {}
graph = defaultdict(list)

def dfs(curr, visited):
  if not graph[curr]:
    whos_boss[visited[-1]] = visited[::-1]
    return
  elif curr not in whos_boss:
    whos_boss[curr] = visited[::-1]
    
  for next in graph[curr]:
    if next not in visited:
      dfs(next, visited + [next])
  
  

def solution(enroll, referral, seller, amount):
  
  for i in range(len(referral)):
    graph[referral[i]].append(enroll[i])

  dfs('-', ['-'])

  profits = {}
  for i in range(len(seller)):
    total = amount[i] * 100
    if total <= 0:
      continue
    
    for boss in whos_boss[seller[i]]:
      if boss not in profits:
        profits[boss] = 0
        
      if boss == '-' or total <= 0:
        break
      elif total // 10 == 0:
        profits[boss] += total
        break
      else:
        profits[boss] += total - (total // 10)
        total //= 10

        
  result = []
  for i in range(len(enroll)):
    if enroll[i] not in profits:
      result.append(0)
    else:
      result.append(profits[enroll[i]])

  return result
