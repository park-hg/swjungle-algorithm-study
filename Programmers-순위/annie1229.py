from collections import deque

def solution(n, results):
  answer = 0
  win = [[] for _ in range(n+1)]
  lose = [[] for _ in range(n+1)]
  for result in results:
    win[result[0]].append(result[1])
    lose[result[1]].append(result[0])
  
  for i in range(1, n+1):
    check = [False for _ in range(n+1)]
    count_win = 0
    q = deque(win[i])
    for ii in win[i]:
      check[ii] = True
    while q:
      pop = q.popleft()
      count_win += 1
      for nn in win[pop]:
        if not check[nn]:
          check[nn] = True
          q.append(nn)
          
    check = [False for _ in range(n+1)]
    count_lose = 0
    q = deque(lose[i])
    for ii in lose[i]:
      check[ii] = True
    while q:
      pop = q.popleft()
      count_lose += 1
      for nn in lose[pop]:
        if not check[nn]:
          check[nn] = True
          q.append(nn)

    if count_win + count_lose == n-1:
      answer += 1
      
  return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])