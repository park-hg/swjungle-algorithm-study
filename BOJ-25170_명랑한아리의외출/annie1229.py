# 명랑한 아리의 외출(BOJ-25170)
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M, T = map(int, input().split())
work_amount = []
work_time = []
for n in range(N):
  work_amount.append(list(map(int, input().split())))
for n in range(N):
  work_time.append(list(map(int, input().split())))

print(work_amount)
print(work_time)
# 일단은 bfs로 최단거리로 갔을 때 걸리는 시간 구하고 남은 시간만큼 할 수 있는 일 중에 최대

def bfs(start):
  q = deque()
  q.append((start, 0, 0))
  dx = [0, 1, 1]
  dy = [1, 1, 0]
  dp = [[0 for _ in range(M)] for _ in range(N)]
  max_amount = 0
  while q:
    point, count, amount = q.popleft()
    if T <= count:
      continue
    x = point[0]
    y = point[1]
    dp[x][y] = max(dp[x][y], amount)
    for i in range(3):
      new_x = x + dx[i]
      new_y = y + dy[i]
      if new_x == N-1 and new_y == M-1:
        max_amount = max(max_amount, amount)
        # print('도착지까지 이동 시간', count + 1, '남은 시간', T - count - 1, '한 일', amount)
      if new_x < N and new_y < M:
        q.append(([new_x, new_y], count + 1, amount))
        q.append(([new_x, new_y], count + 1 + work_time[new_x][new_y], amount + work_amount[new_x][new_y]))
  print('max amount >> ', max_amount)
  return max_amount
bfs([0, 0])

