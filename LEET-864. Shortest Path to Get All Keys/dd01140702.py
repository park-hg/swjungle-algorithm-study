from collections import deque

grid = ["@.a..","###.#","b.A.B"]
start = False
key_num = 0
key = [False]
lock = [False]

r = len(grid)
c = len(grid[0])

box = [[-1]*(key_num+1) for _ in range(key_num +1)]

for i in range(len(r)):
    for j in range(len(c)):
        now = grid[i][j]
        if now == '.' or now == '#':
            continue
        elif now.isupper():
            key_num += 1
            key.append((i,j))
        elif now.islower():
            lock.append((i,j))
        elif now == '@':
            grid[i,j] = '.'
            start = (i,j)

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find(left,right,key_list):
    q = deque([(left,right)])
    visit = [([False]*c) for _ in range(r)]
    visit[q[0][0]][q[0][1]] = True

    while q :
        n_r,n_c = q.popleft()

        if visit[n_r][n_c] :
            i