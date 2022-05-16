# 18. 두 동전(BOJ-16197) # 아직 푸는 중입니다.. 다시 풀어서 올리겠습니다!
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

print(board)
print(coins)
def bfs():
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q.append((coins[0], coins[1], 1))
    while q:
        coin1, coin2, count = q.popleft()
        # print('coin1 ', coin1, 'coin2', coin2, count)
        x1, y1 = coin1
        x2, y2 = coin2
        
        if count >= 10:
            break

        for n in range(4):
            next_x1 = x1 + dx[n]
            next_y1 = y1 + dy[n]
            next_x2 = x2 + dx[n]
            next_y2 = y2 + dy[n]

            if board[next_x1][next_y1] == '#':
                next_x1 = x1
                next_y1 = y1
            if board[next_x2][next_y2] == '#':
                next_x2 = x2
                next_y2 = y2

            if next_x1 >= 0 and next_y1 >= 0 and next_x1 < N and next_y1 < M:
                if next_x2 >= 0 and next_y2 >= 0 and next_x2 < N and next_y2 < M:
                    next_coin1 = (next_x1, next_y1)
                    next_coin2 = (next_x2, next_y2)
                    if next_coin1 != next_coin2:
                        q.append((next_coin1, next_coin2, count+1))
                else:
                    print(n, '동전2가 떨어졌습니다.', count + 1)
            else:
                if next_x2 >= 0 and next_y2 >= 0 and next_x2 < N and next_y2 < M and board[next_x2][next_y2] != '#':
                    print(n, '동전1이 떨어졌습니다.', count + 1)
    print(count)
bfs()
