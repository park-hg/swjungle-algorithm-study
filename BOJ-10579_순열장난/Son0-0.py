import sys

input = sys.stdin.readline

num = input().strip()


def solution():

    length = len(num)
    N = 9 + ((length - 9) // 2)

    if N < 10:
        print(*num)
        return

    def dfs(length, visited=[]):
        if N == len(visited):
            print(*visited)
            exit(0)

        if 1 <= int(num[length]) <= N and int(num[length]) not in visited:
            dfs(length + 1, visited + [int(num[length])])
        if 1 <= int(num[length:length + 2]) <= N and int(num[length:length + 2]) not in visited:
            dfs(length + 2, visited + [int(num[length:length + 2])])

    dfs(0, [])

solution()
