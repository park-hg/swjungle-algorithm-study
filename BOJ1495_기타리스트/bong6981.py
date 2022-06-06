import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
nums = list(map(int, input().split()))


can = [S]
ans = 0
for num in nums:
    print(num, can)
    new_can = set()
    for c in can:
        print(c, c-num, c+num)
        if 0<= (c + num) <= M:
            new_can.add(c+num)
        if 0 <= (c - num) <= M:
            new_can.add(c-num)
    can = new_can
    if len(new_can) == 0:
        ans = -1
        break
if ans == -1:
    print(ans)
else:
    print(max(can))

