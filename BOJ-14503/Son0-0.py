# 왜 틀렸죠?

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
start = list(map(int, input().split()))
_map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(x, y, cnt, dir):

    for i in range(4):
        tdir = (dir + 3 - i) % 4
        nx, ny = x + dx[tdir], y + dy[tdir]
        if 0 <= nx < M and 0 <= ny < N:
            if _map[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                return dfs(nx, ny, cnt + 1, tdir)

    nx, ny = x - dx[dir], y - dy[dir]
    if _map[nx][ny] == 1:
        return cnt
    else:
        return dfs(nx, ny, cnt, dir)


def solution():
    visited[start[0] - 1][start[1] - 1] = 1
    return dfs(start[0] - 1, start[1] - 1, 1, start[2])


print(solution())
