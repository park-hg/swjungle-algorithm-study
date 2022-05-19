# 21. 음악프로그램(BOJ-2623)
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
order_list = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
result = []

for _ in range(M):
    num, *arr = list(map(int, input().split()))
    for i in range(1, num):
        order_list[arr[i-1]].append(arr[i])
        indegree[arr[i]] += 1

q = deque()
for n in range(1, N + 1):
    if indegree[n] == 0:
        q.append(n)

while q:
    pop = q.popleft()
    result.append(pop)
    for i in order_list[pop]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) == N:
    print('\n'.join(list(map(str, result))))
else:
    print(0)


