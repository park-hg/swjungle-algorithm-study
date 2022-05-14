import sys

sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = r, c
cur_d = d
ans = 0

cnt = 0
while True:
    grid[x][y] = 1
    ans += 1

    tmp_x, tmp_y = x+dx[(cur_d-1)%4], y+dy[(cur_d-1)%4]
    if 0 <= tmp_x < N and 0 <= tmp_y < M and grid[tmp_x][tmp_y] == 0:
        x, y = tmp_x, tmp_y
        cur_d = (cur_d-1)%4
    else:
        cur_d = (cur_d-1)%4
        cnt += 1
    
    if cnt == 4:
        


    