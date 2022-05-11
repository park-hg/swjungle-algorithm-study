import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

names = set()
for _ in range(N):
    names.add(sys.stdin.readline().rstrip())

ans = []
for name in names:
    cur = sys.stdin.readline().rstrip()
    if cur in names:
        ans.append(cur)

ans.sort()
print(len(ans))
for name in ans:
    print(name)