import sys
from collections import deque
sys.stdin = open('input.txt')

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
visited = [[[-1]*W for _ in range(H)] for _ in range(K+1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ddx = [-1, -2, -2, -1, 1, 2, 2, 1]
ddy = [2, 1, -1, -2, -2, -1, 1, 2]

que = deque([[0, 0, K, 0]])
visited[K][0][0] = 0
answer = 1e9
while que:
    x, y, k, cnt = que.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < H and 0 <= ny < W and visited[k][nx][ny] == -1:
            if grid[nx][ny] != 1:
                que.append([nx, ny, k, cnt+1])
                visited[k][nx][ny] = cnt+1
    if k > 0:
        for j in range(8):
            nx, ny = x+ddx[j], y+ddy[j]
            if 0 <= nx < H and 0 <= ny < W and visited[k-1][nx][ny] == -1:
                if grid[nx][ny] != 1:
                    que.append([nx, ny, k-1, cnt+1])
                    visited[k-1][nx][ny] = cnt+1

answer = 1e9
for k in range(K+1):
    answer = min(answer, visited[k][-1][-1])

print(answer)