import sys

input = sys.stdin.readline

S, C = map(int, input().split())
plen = [int(input()) for _ in range(S)]
result = 0


def calc(target):
    cnt = 0
    for p in plen:
        cnt += p // target
        if C <= cnt:
            return True

    return False


def bin_search(left, right):
    if right < left:
        return

    mid = (left + right) // 2

    if calc(mid):
        global result
        result = mid
        bin_search(mid + 1, right)
    else:
        bin_search(left, mid - 1)


def solution():
    bin_search(1, max(plen))
    print(sum(plen) - (result * C))


solution()
