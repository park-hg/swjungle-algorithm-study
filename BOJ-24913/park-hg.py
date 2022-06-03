import sys
sys.stdin = open('input.txt')

N, Q = map(int, sys.stdin.readline().split())
others = [0]*N
me = 0
max_c, min_c = 0, 1e9

for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        x, p = query[1:]
        if p == N+1:
            me += x
        else:
            others[p-1] += x
            max_c = max(others[p-1], max_c)
            min_c = min(others[p-1], min_c)

    elif query[0] == 2:
        x, y = query[1:]
        if max_c*N - sum(others) > y:
            if me+x > max_c:
                print("YES")
            else:
                print("NO")
        else:
            l = max(0, y - max_c*N + sum(others))
            q, r = int(l/N), l%N
            if me + x > max_c + q + (l%N > 0):
                print("YES")
            else:
                print("NO")