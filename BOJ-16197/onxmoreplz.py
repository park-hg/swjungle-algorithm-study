import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  while queue:
    x1, y1, x2, y2, cnt = queue.popleft()
    if cnt >= 10:
      return -1
  
    for dir in range(4):
      nx1, ny1 = x1 + dx[dir], y1 + dy[dir]
      nx2, ny2 = x2 + dx[dir], y2 + dy[dir]
      if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
        if arr[nx1][ny1] == '#':
          nx1, ny1 = x1, y1
        if arr[nx2][ny2] == '#':
          nx2, ny2 = x2, y2
        queue.append((nx1, ny1, nx2, ny2, cnt + 1))
      elif 0 <= nx1 < N and 0 <= ny1 < M:
        return cnt + 1
      elif 0 <= nx2 < N and 0 <= ny2 < M:
        return cnt + 1
      else:
        continue

  return -1

N, M = map(int, sys.stdin.readline().split())
coins = []
arr = []

for i in range(N):
  inputs = list(sys.stdin.readline().strip())
  arr.append(inputs)
  if inputs.count('o') == 1:
    coins.append(i)
    coins.append(inputs.index('o'))
  elif inputs.count('o') == 2:
    coins.append(i)
    coins.append(inputs.index('o'))
    coins.append(i)
    coins.append(len(inputs) - inputs[::-1].index('o') - 1)
  
queue = deque()
queue.append((coins[0], coins[1], coins[2], coins[3], 0))


print(bfs())
