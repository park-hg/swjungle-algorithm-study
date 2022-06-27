import sys

dx = [-1, 0, 1]
dy = [1, 1, 1]

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]


def dfs(row, col):
  global answer
  if col == C - 1:
    answer += 1
    return True

  for dir in range(3):
    nx = row + dx[dir]
    ny = col + dy[dir]

    if 0 <= nx < R and 0 <= ny < C:
      if board[nx][ny] == '.' and visited[nx][ny] == -1:
        visited[nx][ny] = 1
        if dfs(nx, ny):
          return True
  return False
          

answer = 0
for i in range(R):
  visited[i][0] = 1
  dfs(i, 0)
  visited[i][0] = -1

print(answer)
