from collections import deque

def check_count(arr, idx, n):
  check = [False for _ in range(n+1)]
  count = 0
  q = deque(arr[idx])
  for i in arr[idx]:
    check[i] = True
  while q:
    pop = q.popleft()
    count += 1
    for p in arr[pop]:
      if not check[p]:
        check[p] = True
        q.append(p)
  return count

def solution(n, results):
  answer = 0
  win = [[] for _ in range(n+1)]
  lose = [[] for _ in range(n+1)]

  for result in results:
    win[result[0]].append(result[1])
    lose[result[1]].append(result[0])
  
  for i in range(1, n+1):
    count_win = check_count(win, i, n)
    count_lose = check_count(lose, i, n)
    if count_win + count_lose == n-1:
      answer += 1

  print(answer)
  return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])