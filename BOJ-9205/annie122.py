# 25. 맥주 마시면서 걸어가기(BOJ-9205)
import sys
from collections import deque
sys.stdin = open('input.txt');
input = sys.stdin.readline
max_distance = 1000
test_count = int(input())

def calc_dist(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def bfs(n, start, dests):
    q = deque()
    q.append(start)
    visited = [False for _ in range(n)]

    while q:
        pop = q.popleft()
        for idx, d in enumerate(dests):
            if not visited[idx] and calc_dist(pop, d) <= max_distance:
                if idx == n - 1:
                    return 'happy'
                visited[idx] = True
                q.append(d)
    return 'sad'

for n in range(test_count):
    store_count = int(input())
    start_point = list(map(int, input().split()))
    destinations = []
    for _ in range(store_count):
        destinations.append(list(map(int, input().split())))
    destinations.append(list(map(int, input().split())))
    print(bfs(store_count + 1, start_point, destinations))
    
