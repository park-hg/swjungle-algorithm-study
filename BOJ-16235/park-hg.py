import sys
from collections import defaultdict
sys.stdin = open('input.txt')
N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trees = defaultdict(list)

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    trees[(x, y)].append(z)

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

grid = [[5]*N for _ in range(N)]
for _ in range(K):

    for (x, y) in trees:
        trees[(x, y)].sort()
        new_trees = []
        died = 0
        for tree in trees[(x, y)]:
            if tree <= grid[x][y]:
                new_trees.append(tree+1)
                grid[x][y] -= tree
            else:
                died += tree//2
        
        trees[(x, y)] = new_trees

        grid[x][y] += died
    

    cur_trees = [(x, y) for (x, y) in trees]
    for (x, y) in cur_trees:
        for tree in trees[(x, y)]:
            if tree%5 == 0:
                for i in range(8):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        trees[(nx, ny)].append(1)

    for x in range(N):
        for y in range(N):
            grid[x][y] += A[x][y]
    
ans = 0 
for (x, y) in trees:
    ans += len(trees[((x, y))])

print(ans)
                


    
    

