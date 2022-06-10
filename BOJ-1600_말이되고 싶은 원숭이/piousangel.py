import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

k = int(input())

col, row = map(int, input().split())

visited = [[False] * col for i in range(row)]
board = []
for i in range(row) :
    board.append(list(map(int, input().split())))


def bfs(board, visited, k) :
    global answer
    q = deque()

    q.append([0,0,0,k])
    visited[0][0] = True
    while q :
        
        y, x, cnt, k = q.popleft()

        if x == len(board[0]) - 1 and y == len(board)-1 :
            answer = min(answer, cnt)

        if k > 0 :
            # chkhorse(x, y, board, visited)
            if 0 <= x - 2 < len(board[0]) and 0 <= y - 1 < len(board) :
                nx = x - 2
                ny = y - 1
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])

            if 0 <= x - 1 < len(board[0]) and 0 <= y - 2 < len(board) :
                nx = x - 1
                ny = y - 2
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
            if 0 <= x + 1 < len(board[0]) and 0 <= y - 2 < len(board) :
                nx = x + 1
                ny = y - 2
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
            if 0 <= x + 2 < len(board[0]) and 0 <= y + 1 < len(board) :
                nx = x + 2
                ny = y + 1
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
            if 0 <= x + 2 < len(board[0]) and 0 <= y + 1 < len(board) :
                nx = x + 2
                ny = y + 1
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
            if 0 <= x + 1 < len(board[0]) and 0 <= y + 2 < len(board) :
                nx = x + 1
                ny = y + 2
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
            if 0 <= x - 1 < len(board[0]) and 0 <= y + 2 < len(board) :
                nx = x - 1
                ny = y + 2
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
            if 0 <= x - 2 < len(board[0]) and 0 <= y + 1 < len(board) :
                nx = x - 2
                ny = y + 1
                if board[ny][nx] != 1 and visited[ny][nx] == False :
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1, k-1])
                
        else:
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) :
                    if board[ny][nx] != 1 and visited[ny][nx] == False :
                        visited[ny][nx] = True
                        q.append([ny,nx,cnt+1, k])

answer = 10000001
bfs(board, visited, k)
if answer == 10000001 :
    print(-1)
else:
    print(answer)