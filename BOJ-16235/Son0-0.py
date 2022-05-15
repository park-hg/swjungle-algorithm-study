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

new_tree = []

for _ in range(M):
    t = list(map(int, input().split()))
    idx = str(t[0] - 1) + str(t[1] - 1)
    tree[idx].append(t[2])

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def ss():
    for tt in tree:
        if tree[tt]:
            temp = []
            dead, tcnt = 0, 0
            tree[tt].sort(reverse=True)
            while tree[tt]:
                t = tree[tt].pop()
                if t <= flist[tt]:
                    flist[tt] -= t
                    t += 1
                    if t % 5 == 0:
                        tcnt += 1
                    temp.append(t)
                else:
                    dead += t // 2
            if tcnt != 0:
                new_tree.append((int(tt[0]), int(tt[1]), tcnt))
            tree[tt] = temp
            flist[tt] += dead
        flist[tt] += A[int(tt[0])][int(tt[1])]


def fall():
    while new_tree:
        t = new_tree.pop()
        for i in range(8):
            nx, ny = t[0] + dx[i], t[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                idx = str(nx) + str(ny)
                for _ in range(t[2]):
                    tree[idx].append(1)


def solution(K):
    while K != 0:
        # spring summer winter
        ss()
        # fall
        if new_tree:
            fall()
        K -= 1

    cnt = 0
    for t in tree:
        cnt += len(tree[t])
    print(cnt)


solution(K)
