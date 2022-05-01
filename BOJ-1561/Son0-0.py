import sys

input = sys.stdin.readline

N, M = map(int, input().split())
llist = list(map(int, input().split()))
time, pos = 0, 0


def calc(target):
    result = 0

    for due in llist:
        temp = (target / due) - (target // due)
        if 0 < temp:
            result += (target // due) + 1
        else:
            result += (target // due)

    return result


def bin_search(left, right):
    global time, pos

    if right < left:
        return

    mid = (left + right) // 2

    calc_data = calc(mid)

    if calc_data < N:
        if time < mid:
            time = mid
            pos = calc_data
        bin_search(mid + 1, right)
    else:
        bin_search(left, mid - 1)


def solution():
    global time, pos
    max_time = max(list(set(llist))) * N

    if N <= M:
        print(N)
    else:
        bin_search(0, max_time)
        for idx, size in enumerate(llist):
            if time % size == 0:
                pos += 1
                if pos == N:
                    print(idx + 1)
                    break


solution()
