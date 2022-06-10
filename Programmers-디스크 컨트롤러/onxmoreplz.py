import heapq

def solution(jobs):
  heap = []
  times = []
  for start, long in jobs:
    heapq.heappush(heap, (long, start))
    times.append(start)

  answer = 0
  temp_heap = []
  now = min(times)
  while heap:
    if now < min(times):
      now = min(times)
    long, start = heapq.heappop(heap)
    if start > now:
      heapq.heappush(temp_heap, (long, start))
      continue
    else:
      now += long
      answer += (now - start)
      times.remove(start)
      while temp_heap:
        heapq.heappush(heap, heapq.heappop(temp_heap))

  answer //= len(jobs) 

  print(answer)
  return answer
