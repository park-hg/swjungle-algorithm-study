# 
# https://www.acmicpc.net/problem/16235

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

tree = dict()
for row in range(N):
    for col in range(N):
        tree[str(row)+str(col)] = []

flist = dict()
for row in range(N):
    for col in range(N):
        flist[str(row)+str(col)] = 5

for _ in range(M):
    t = list(map(int, input().split()))
    tree[str(t[0] - 1) + str(t[1] - 1)].append(t[2])

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def ss():
    for row in range(N):
        for col in range(N):
            idx = str(row) + str(col)
            if tree[idx]:
                temp = []
                tree[idx].sort(reverse=True)
                while tree[idx]:
                    t = tree[idx].pop()
                    if t <= flist[idx]:
                        flist[idx] -= t
                        t += 1
                        temp.append(t)
                    else:
                        flist[idx] += (t // 2)
                tree[idx] = temp


def fw():

    for x in range(N):
        for y in range(N):
            idx = str(x) + str(y)
            flist[idx] += A[x][y]
            for t in tree[idx]:
                if (t % 5) == 0:
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            idx = str(nx) + str(ny)
                            tree[idx].append(1)


def solution():
    global K

    while K != 0:
        # spring summer
        ss()
        # fall winter
        fw()
        K -= 1

    cnt = 0
    for t in tree:
        cnt += len(tree[t])
    print(cnt)


solution()
