import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

_map = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

temp = []
for i in range(N):
    data = list(map(str, input().strip()))
    for j in range(M):
        if data[j] == 'o':
            temp.append(i)
            temp.append(j)
    _map.append(data)

coin = deque()
coin.append([temp[0], temp[1], temp[2], temp[3]])


def bfs():
    cnt = 1

    while coin:
        if 10 < cnt:
            print(-1)
            return

        for _ in range(len(coin)):
            c = coin.popleft()

            for i in range(4):
                n1x, n1y = c[0] + dx[i], c[1] + dy[i]
                n2x, n2y = c[2] + dx[i], c[3] + dy[i]
                if ((n1x < 0 or N <= n1x) or (n1y < 0 or M <= n1y)) and ((n2x < 0 or N <= n2x) or (n2y < 0 or M <= n2y)):
                    continue

                if ((n1x < 0 or N <= n1x) or (n1y < 0 or M <= n1y)) and (0 <= n2x < N and 0 <= n2y < M):
                    print(cnt)
                    return

                if ((n2x < 0 or N <= n2x) or (n2y < 0 or M <= n2y)) and (0 <= n1x < N and 0 <= n1y < M):
                    print(cnt)
                    return

                if 0 <= n1x < N and 0 <= n1y < M and 0 <= n2x < N and 0 <= n2y < M:
                    if _map[n1x][n1y] == '#':
                        n1x, n1y = c[0], c[1]
                    if _map[n2x][n2y] == '#':
                        n2x, n2y = c[2], c[3]

                    if n1x == n2x and n1y == n2y:
                        continue

                    coin.append([n1x, n1y, n2x, n2y])
        cnt += 1


def solution():
    bfs()


solution()
