import sys

input = sys.stdin.readline

# n: 곡의 개수 s: 시작 볼륨 m: 볼륨 리밋
n, s, m = map(int, input().split())
vlist = list(map(int, input().split()))

visited = [[0 for _ in range(m + 1)] for _ in range(n)]


def solution():
    max_value = -1

    if 0 <= s + vlist[0] <= m:
        visited[0][s + vlist[0]] = 1
        if n == 1:
            max_value = max(max_value, s + vlist[0])
    if 0 <= s - vlist[0] <= m:
        visited[0][s - vlist[0]] = 1
        if n == 1:
            max_value = max(max_value, s - vlist[0])

    for idx, volume in enumerate(vlist):
        if idx == 0:
            continue
        else:
            for i in range(m + 1):
                if visited[idx - 1][i] == 1:
                    if 0 <= i + volume <= m:
                        visited[idx][i + volume] = 1
                        if idx == n - 1:
                            max_value = max(max_value, i + volume)
                    if 0 <= i - volume <= m:
                        visited[idx][i - volume] = 1
                        if idx == n - 1:
                            max_value = max(max_value, i - volume)

    print(max_value)


solution()
