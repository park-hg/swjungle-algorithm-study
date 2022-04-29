#https://www.acmicpc.net/problem/1897
from collections import defaultdict, deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

d, word = input().rstrip().split()
d = int(d)

dic = defaultdict(list)

for _ in range(d):
    w = input().rstrip()
    dic[len(w)].append(w)

left = deque([word])
ans = ''

def find(short, long):
    cnt = 1
    long = deque(list(long)) 
    idx = 0
    while long:
        if idx == len(short) and cnt == 1 and len(long) == 1:
            return True

        now = long.popleft()
        if short[idx] == now:
            idx += 1
        else:
            if cnt > 0:
                cnt -= 1
                continue
            else:
                return False
    return True


while left:
    now = left.popleft()
    ans = now
    if len(now) + 1 not in dic:
        break

    for w in dic[len(now)+1]:
        if w not in left and find(now, w):
            left.append(w)

print(ans)
