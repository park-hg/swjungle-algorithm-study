import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx_h = [-2, -1, 1, 2, -2, -1, 1, 2]
dy_h = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
  queue = deque()
  queue.append((0, 0, 0, K))
  while queue:
    x, y, step, curr_k = queue.popleft()

    if curr_k > 0:
      for dir in range(8):
        nx, ny = x + dx_h[dir], y + dy_h[dir]
        if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] == 0:
          if visited[nx][ny] == -1 or visited[nx][ny] < curr_k - 1:
            if nx == H - 1 and ny == W - 1:
              return step + 1
            visited[nx][ny] = curr_k - 1
            queue.append((nx, ny, step + 1, curr_k - 1))
              
    for dir in range(4):
      nx, ny = x + dx[dir], y + dy[dir]
      if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] == 0:
        if visited[nx][ny] == -1 or visited[nx][ny] < curr_k:
          if nx == H - 1 and ny == W - 1:
            return step + 1
          visited[nx][ny] = curr_k
          queue.append((nx, ny, step + 1, curr_k))

  return -1

  
K = int(sys.stdin.readline().strip())
W, H = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
visited = [[-1] * W for _ in range(H)]

if W == 1 and H == 1:
  print(0)
else:
  print(bfs())
