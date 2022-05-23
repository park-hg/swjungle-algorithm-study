from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    q= deque()
    c = []
    q.append([x, y, 20])
    c.append([x, y, 20])

    while q:
        x, y, beer = q.popleft()
        if x == x1 and y == y1:
            print("happy")
            return

        for nx, ny in d:
            if [nx, ny, 20] not in c:
                l1 = abs(nx - x) + abs(ny - y)
                if beer * 50 >= l1:
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return

tc = int(input())
while tc:

    n = int(input())
    x0, y0 = map(int, input().split())
    d = []
    for _ in range(n):
        x, y = map(int, input().split())
        d.append([x, y])
    x1, y1 = map(int, input().split())
    d.append([x1, y1])
    bfs(x0, y0)