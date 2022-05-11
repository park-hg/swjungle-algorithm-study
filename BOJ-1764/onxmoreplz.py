import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
dut = sorted([sys.stdin.readline().strip() for _ in range(N)])
bo = defaultdict(list)

for _ in range(M):
  bo[sys.stdin.readline().strip()]

answer = []
for d in dut:
  if d in bo:
    answer.append(d)

print(len(answer))
print(*answer, sep = '\n')
