import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline


# 0 북, 1 동, 2 남, 3 서

move_d = {0 : (-1, 0), 1 : (0, -1), 2 : (1, 0), 3 : (0, 1)} # 

row, col = map(int, input().split())
r, c, d = map(int, input().split())

board = []
visited = [[False]*(col) for _ in range(row)]
answer = 1

for i in range(row):
    board.append(list(map(int, input().split())))

# print(visited)
# print(board)
# print(move_d[1])
# print(visited)

def find_robot(board, visited, r, c, d) :
    global answer
    visited[r][c] = True
    q = deque()

    q.append([r, c, d, 1, 0])

    while q :

        now_r, now_c, now_d, cnt, now_a = q.popleft()
        print("행, 열", now_r, now_c)
        # print("now_d", now_d)
        # print(now_a)
        answer = max(answer, cnt)
        next_r = now_r + move_d[now_d][1] #row
        next_c = now_c + move_d[now_d][0] #col

        if visited[next_r][next_c] != True and board[next_r][next_c] == 0 :
            if now_d == 0 :
                visited[next_r][next_c] = True
                q.append([next_r, next_c, 3, cnt + 1, 0])
            else:
                visited[next_r][next_c] = True
                q.append([next_r, next_c, now_d-1, cnt + 1, 0])
        else:
            if now_a < 4 :   #방향 바꿔주고, now_a만 늘려주기
                if now_d == 0 :
                    q.append([now_r, now_c, 3, cnt , now_a + 1])
                else:
                    q.append([now_r, now_c, now_d-1, cnt , now_a + 1])
            else:  # 4번 진행되었을 때 후진한다

                # if now_d == 0 :
                #     now_d = 3
                #     next_r = now_r + move_d[now_d][1]
                #     next_c = now_c + move_d[now_d][0]
                # else:
                #     now_d -= 1
                #     next_r = now_r + move_d[now_d][1]
                #     next_c = now_c + move_d[now_d][0]

                temp_r = now_r - move_d[now_d][1]
                temp_c = now_c - move_d[now_d][0]
                
                if visited[temp_r][temp_c] != True and board[temp_r][temp_c] == 0 :
                    visited[temp_r][temp_c] = True
                    if now_d == 0 :
                        q.append([temp_r, temp_c, 3, cnt + 1, 0])
                    else:
                        q.append([temp_r, temp_c, now_d-1, cnt + 1, 0])
                else:
                    break

  
find_robot(board, visited, r, c, d)
print(answer)

