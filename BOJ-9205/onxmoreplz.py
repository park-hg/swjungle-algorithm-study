# Boj - 9205(맥주 마시면서 걸어가기)

import sys
from collections import deque

def bfs():
  queue = deque()
  visited.append((home_x, home_y))
  queue.append((home_x, home_y))
  
  while queue:
    curr_x, curr_y = queue.popleft()
  
    if abs(fest_x - curr_x) + abs(fest_y - curr_y) <= 1000:
      return True
  
    for cand in market:
      if abs(cand[0] - curr_x) + abs(cand[1] - curr_y) <= 1000:
        if (cand[0], cand[1]) not in visited:
          visited.append((cand[0], cand[1]))
          queue.append((cand[0], cand[1]))

t = int(sys.stdin.readline().strip())
for _ in range(t):
  cnt = int(sys.stdin.readline().strip())
  home_x, home_y = map(int, sys.stdin.readline().split())
  market = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]
  fest_x, fest_y = map(int, sys.stdin.readline().split())
  
  visited = []
  
  if bfs():
    print("happy")
  else:
    print("sad")
