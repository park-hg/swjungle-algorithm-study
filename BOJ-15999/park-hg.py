import sys
from collections import deque
sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def bfs(s, t):
    que = deque([[s, t]])
    visited[s][t] = True
    cnt = 0
    while que:
        x, y = que.popleft()
        flag = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == grid[x][y]:
                    if not visited[nx][ny]:
                        que.append([nx, ny])
                        visited[nx][ny] = True
                else:
                    flag = False
        if flag:
            cnt += 1
    
    return cnt

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans += bfs(i, j)

print(pow(2, ans, 10**9+7))
