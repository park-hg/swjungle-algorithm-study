# 왜 틀렸죠?

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
start = list(map(int, input().split()))
_map = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def dfs(x, y, dir, cnt):
    if _map[x][y] == 0:
        _map[x][y] = -1
        cnt += 1

    for i in range(4):
        tdir = (dir + 3 - i) % 4
        nx, ny = x + dx[tdir], y + dy[tdir]
        if 0 <= nx < N and 0 <= ny < M:
            if _map[nx][ny] == 0:
                return dfs(nx, ny, tdir, cnt)

    nx, ny = x - dx[dir], y - dy[dir]
    if _map[nx][ny] == 1: return cnt
    return dfs(nx, ny, dir, cnt)


def solution():
    x, y, dir = start[0], start[1], start[2]

    print(dfs(x, y, dir, 0))


solution()
