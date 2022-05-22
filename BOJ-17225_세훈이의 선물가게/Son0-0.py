# 부분성공, 푸는중입니다.

import sys, heapq

input = sys.stdin.readline

sangmin_time, jisoo_time, N = map(int, input().split())
pnum = 0

def solution():

  pq = []
  sptr, jptr = 0, 0
  for _ in range(N):
    t, color, count = map(str, input().split())
    t, count = int(t), int(count)
    for _ in range(count):
      if color == 'B':
        if t < sptr:
          heapq.heappush(pq, (sptr, 'B'))
        else:
          heapq.heappush(pq, (t, 'B'))
        sptr += sangmin_time
        t += sangmin_time
      else:
        if t < jptr:
          heapq.heappush(pq, (jptr, 'R'))
        else:
          heapq.heappush(pq, (t, 'R'))
        jptr += jisoo_time
        t += jisoo_time
        
  cnt = 1
  sangmin_list, jisoo_list = [], []
  while pq:
    dummy, color = heapq.heappop(pq)
    if color == 'B':
      sangmin_list.append(cnt)
    else:
      jisoo_list.append(cnt)
    cnt += 1
      
  print(len(sangmin_list))
  print(*sangmin_list, sep=' ')
  
  print(len(jisoo_list))
  print(*jisoo_list, sep=' ')
  
  return 0
  
solution()
