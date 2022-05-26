import sys
sys.stdin = open('input.txt')

N, S = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))


if sum(a) < S:
    print(0)
    exit()

s = [0]
sub_sum = 0
for i in range(N):
    sub_sum += a[i]
    s.append(sub_sum)

left, right = 0, 1
answer = len(s)
while left < right < len(s):
    if s[right] - s[left] < S:
        right += 1
    else:
        answer = min(answer, right-left)
        left += 1


print(answer)