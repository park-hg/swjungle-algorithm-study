N, M = map(int, input().split())

didnt_listen = set()
didnt_see = set()

for _ in range(N):
    didnt_listen.add(input())

for _ in range(M):
    didnt_see.add(input())

ans = sorted(list(didnt_listen & didnt_see))
print(len(ans))
for name in ans:
    print(name)
