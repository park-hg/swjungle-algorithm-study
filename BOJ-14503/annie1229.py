# 16. 로봇청소기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(rr, cc, dir):
    global clean_count
    global rotation_count
    
    visited[rr][cc] = True

    next_rr = rr
    next_cc = cc

    if dir == 0:
        next_cc -= 1
    elif dir == 1:
        next_rr -= 1
    elif dir == 2:
        next_cc += 1
    else:
        next_rr += 1

    dir = (dir + 3) % 4
    
    if next_rr >= 0 and next_cc >= 0 and next_rr < N and next_cc < M and not visited[next_rr][next_cc] and room_map[next_rr][next_cc] == 0:
        rotation_count = 0
        clean_count += 1
        dfs(next_rr, next_cc, dir)
    else:
        rotation_count += 1
    
    if rotation_count > 3:
        if dir == 0:
            rr += 1
        elif dir == 1:
            cc -= 1
        elif dir == 2:
            rr -= 1
        else:
            cc += 1

        if room_map[rr][cc]:
            print(clean_count)
            exit(0)
        else:
            rotation_count = 0
    dfs(rr, cc, dir)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room_map = []
for _ in range(N):
    room_map.append(list(map(int, input().split())))

clean_count = 1
rotation_count = 0
visited = [[False for _ in range(M)] for _ in range(N)]

dfs(r, c, d)
