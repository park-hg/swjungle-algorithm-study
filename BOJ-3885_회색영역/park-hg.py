import sys
sys.stdin = open('input.txt')

while True:
    n, w = map(int, sys.stdin.readline().split())
    if n == 0 and w == 0:
        break

    hist = [.0]*11
    for _ in range(n):
        value = int(sys.stdin.readline())
        hist[value//w] += 1

    max_h = .0
    last_idx = .0
    for i in range(11):
        max_h = max(max_h, hist[i])
        if hist[i] > 0:
            last_idx = i

    ans = 0.01
    if last_idx > 0:
        for i in range(11):
            ans += (hist[i]/max_h) * (last_idx-i)/(last_idx)
    else:
        ans += 1

    print(ans)