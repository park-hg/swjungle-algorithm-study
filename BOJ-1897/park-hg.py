import sys
from collections import deque
sys.stdin = open('input.txt')

d, first = sys.stdin.readline().rstrip().split()
d = int(d)
words = [sys.stdin.readline().rstrip() for _ in range(d)]

def check(word, target):
    if len(target) - len(word) != 1:
        return False

    for i in range(len(word)+1):
        if target[:i] + target[(i+1):] in words:
            return True

    return False


que = deque([first])
ans = ''
while que:
    word = que.popleft()
    if len(word) > len(ans):
        ans = word
    for target in words:
        if check(word, target):
            que.append(target)

print(ans)