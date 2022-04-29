import sys
from collections import deque

input = sys.stdin.readline

_input = list(map(str, input().split()))
word = list(_input[1])
wlist = [[] for _ in range(81)]
visited = [0 for _ in range(81)]
max_value = 3
max_length = 0
result = []


def isPossible(str_a, str_b):
    temp_a = deque(str_a)
    temp_b = deque(str_b)

    cnt = 0
    while temp_a:
        if temp_a[0] == temp_b[0]:
            temp_a.popleft()
            temp_b.popleft()
        else:
            cnt += 1
            temp_b.popleft()

        if 1 < cnt:
            return False

    return True


def dfs(cur, length):
    global result, max_value

    if length - 1 == max_length:
        print(*cur, sep='')
        exit(0)

    if max_value < length:
        max_value = length
        result = cur

    for i in range(len(wlist[length])):
        if isPossible(cur, wlist[length][i]):
            dfs(wlist[length][i], length + 1)


def solution():
    global max_length

    for _ in range(int(_input[0])):
        temp = list(input().strip())
        max_length = max(max_length, len(temp))
        wlist[len(temp)].append(temp)

    dfs(word, 4)

    print(*result, sep='')


solution()
