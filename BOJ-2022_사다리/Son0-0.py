import sys

input = sys.stdin.readline

x, y, c = map(float, input().split())


def calc(target):
    hx = (x**2 - target**2)**0.5
    hy = (y**2 - target**2)**0.5
    return (hx * hy) / (hx + hy)


def bin_search(left, right):
    if (right - left) <= 0.0001:
        return left

    mid = (left + right) / 2
    target = calc(mid)

    if target < c:
        return bin_search(left, mid)
    else:
        return bin_search(mid, right)


def solution():
    print(f"{round(bin_search(0, min(x, y)), 3):.3f}")


solution()
