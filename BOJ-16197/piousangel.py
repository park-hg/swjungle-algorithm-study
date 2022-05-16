import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 4개의 버튼, 두개의 빈칸에는 동전이 하나씩 놓여있고, 두 동전의 위치는 다르다
# 동전이 이동하려는 칸이 벽이면 동전은 이동하지 않음
# 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 밖으로 떨어짐
# 동전이 그 위치에 있어도 동전이 이동한다
# 두 동전중 하나만 보드에서 떨어뜨리기 위해 최소 몇번을 눌러야 하나?

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())

board = []

for i in range(N) :
    board.append(list(input().rstrip()))

coin_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o' :
            coin_list.append([i,j])
answer = 10

def bfs(coin_list, board) :
    global answer
    q = deque()
    q.append([coin_list, 0])

    while q :

        now_list, cnt = q.popleft()
        # print("now_list", now_list)
        # print("cnt", cnt)
        # print("len(now_list)", len(now_list))

        if len(now_list) == 1 :
            answer = min(answer, cnt)
            return
        
        if cnt > 10 :
            answer = -1
            break

        coin1_x = now_list[0][1]
        coin1_y = now_list[0][0]
        coin2_x = now_list[1][1]
        coin2_y = now_list[1][0]

        for i in range(4) :
            # print(dx[i], dy[i])
            coin1_nx = coin1_x + dx[i]
            coin1_ny = coin1_y + dy[i]
            coin2_nx = coin2_x + dx[i]
            coin2_ny = coin2_y + dy[i]
            # print(coin1_ny, coin1_nx, coin2_ny, coin2_nx)
            if (0 <= coin1_nx < M and 0 <= coin1_ny < N) and (0 <= coin2_nx < M and 0 <= coin2_ny < N) :
                if board[coin1_ny][coin1_nx] != '#' and board[coin2_ny][coin2_nx] != '#' :  #둘다 노벽
                    q.append([ [ [coin1_ny, coin1_nx], [coin2_ny, coin2_nx] ], cnt+1])
                elif board[coin1_ny][coin1_nx] == '#' and board[coin2_ny][coin2_nx] != '#' : #coin1만 벽
                    q.append([ [ [coin1_y, coin1_x], [coin2_ny, coin2_nx] ], cnt+1])
                elif board[coin1_ny][coin1_nx] != '#' and board[coin2_ny][coin2_nx] == '#' : #coin2만 벽
                    q.append([ [ [coin1_ny, coin1_nx], [coin2_y, coin2_x] ], cnt+1])
            elif (0 <= coin1_nx < M and 0 <= coin1_ny < N) or (0 <= coin2_nx < M and 0 <= coin2_ny < N) :
                q.append([ [[0, 0]], cnt+1])
        # print(q)
    answer = -1
    return

bfs(coin_list, board)
print(answer)

