import sys

d, b = map(int,input().split())

d_list = set([])
ans = set([])

for _ in range(d):
    w = sys.stdin.readline().rstrip()
    d_list.add(w)

for _ in range(b):
    w = sys.stdin.readline().rstrip()
    if w in d_list:
        ans.add(w) 

ans = list(ans)
ans.sort()

print(len(ans))
for i in ans:
    print(i)
