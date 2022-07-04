import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
edges = []
nodes = [list(map(int, sys.stdin.readline().split()))+[i] for i in range(N)]

for i in range(3):
    nodes.sort(key=lambda x:x[i])
    for j in range(N-1):
        edges.append((abs(nodes[j][i]-nodes[j+1][i]), nodes[j][-1], nodes[j+1][-1]))

edges.sort()

par = list(range(N))
rank = [0]*N

def find(x):
    if x == par[x]:
        return x
    return find(par[x])

def unite(x, y):
    x, y = find(x), find(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        if rank[x] == rank[y]:
            rank[x] += 1
        par[y] = x

def same(x, y):
    return find(x) == find(y)

ans = 0
for cost, i, j in edges:
    if not same(i, j):
        unite(i, j)
        ans += cost
        
print(ans)