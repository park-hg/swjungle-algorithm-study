# 20. 구슬 찾기(BOJ-2617)
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
light_beads = [[] for _ in range(N + 1)]
heavy_beads = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    light_beads[A].append(B) # A보다 가벼운 구슬 리스트에 B추가
    heavy_beads[B].append(A) # B보다 무거운 구슬 리스트에 A추가

result = 0
for n in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    light_q = deque([n])
    light_count = 0

    while light_q:
        pop = light_q.popleft()
        visited[pop] = True
        for bead in light_beads[pop]:
            if not visited[bead]:
                visited[bead] = True
                light_q.append(bead)
                light_count += 1

    visited = [False for _ in range(N + 1)]
    heavy_q = deque([n])
    heavy_count = 0

    while heavy_q:
        pop = heavy_q.popleft()
        visited[pop] = True
        for bead in heavy_beads[pop]:
            if not visited[bead]:
                visited[bead] = True
                heavy_q.append(bead)
                heavy_count += 1

    mid = N // 2
    if light_count > mid or heavy_count > mid:
        result += 1 

print(result)