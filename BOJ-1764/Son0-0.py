import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def solution():

    db = {}

    for _ in range(N):
        name = input().strip()
        db[name] = 1

    dbj = []
    cnt = 0
    for _ in range(M):
        name = input().strip()
        if name in db:
            cnt += 1
            dbj.append(name)

    print(cnt)
    print(*sorted(dbj), sep='\n')


solution()
