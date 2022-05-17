# 18. 두 동전(BOJ-16197) 풀이 참고
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
coins = []

for n in range(N):
    line = list(input().rstrip())
    board.append(line)
    for idx, t in enumerate(line):
        if t == 'o':
            coins.append((n, idx))

def is_out(x, y):
    if x >= 0 and x < N and y >= 0 and y < M:
        return False
    return True

def bfs():
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((coins[0], coins[1], 0))

    while q:
        coin1, coin2, count = q.popleft()
        x1, y1 = coin1
        x2, y2 = coin2
        
        if count > 10:
            break

        for n in range(4):
            next_x1 = x1 + dx[n]
            next_y1 = y1 + dy[n]
            next_x2 = x2 + dx[n]
            next_y2 = y2 + dy[n]
            
            is_coin1_out = is_out(next_x1, next_y1)
            is_coin2_out = is_out(next_x2, next_y2)

            if (is_coin1_out and not is_coin2_out) or (not is_coin1_out and is_coin2_out):
                if count + 1 > 10:
                    return -1
                return count + 1
            
            if is_coin1_out and is_coin2_out:
                continue

            if board[next_x1][next_y1] == '#' and board[next_x2][next_y2] == '#':
                continue
            elif board[next_x1][next_y1] == '#':
                next_x1 = x1
                next_y1 = y1
            elif board[next_x2][next_y2] == '#':
                next_x2 = x2
                next_y2 = y2

            q.append(((next_x1, next_y1), (next_x2, next_y2), count + 1))
    return -1

print(bfs())
