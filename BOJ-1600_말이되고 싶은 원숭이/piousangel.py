import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline


k = int(input())
col, row = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dhorseX = [-1, -2, -2, -1, 1, 2, 2, 1]
dhorseY = [-2, -1, 1, 2, 2, 1, -1, -2]

board = []
visited = [[-1]*col for _ in range(row)]
for i in range(row) :
    board.append(list(map(int, input().split())))

# print(board)
# print(visited)

def bfs(board, visited, k) :

    q = deque()
    q.append([0, 0, k, 0])

    while q :

        y, x, k, cnt = q.popleft()

        if x == len(board[0]) - 1 and y == len(board) - 1 :
            return cnt

        if k > 0 :

            for i in range(8) :
                nx = x + dhorseX[i]
                ny = y + dhorseY[i]

                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == 0 :
                    if visited[ny][nx] == -1 or visited[ny][nx] < k - 1:
                        visited[ny][nx] = k - 1
                        q.append([ny, nx, k-1, cnt+1])

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == 0 :
                if visited[ny][nx] == -1 or visited[ny][nx] < k :
                    visited[ny][nx] = k
                    q.append([ny, nx, k, cnt+1])

    return -1

answer = 0
if col == 1 and row == 1 :
    print(0)
else:
    answer = bfs(board, visited, k)
    print(answer)