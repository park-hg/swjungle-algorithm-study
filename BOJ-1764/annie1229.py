# 12. 듣보잡(#1764)
from re import A
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
듣 = set()
answer = []
count = 0

for _ in range(N):
    듣.add(input().rstrip())

for _ in range(M):
    name = input().rstrip()
    if name in 듣:
        answer.append(name)
        count += 1

answer.sort()
print(count)
print("\n".join(answer))