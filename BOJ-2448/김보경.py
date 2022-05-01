n = int(input())
min_tri = [[' ', ' ', '*', ' ', ' '], [' ', '*', ' ', '*', ' '], ['*', '*', '*', '*', '*']]

k = n // 3
graph = [[' '] * (6*k-1) for _ in range(3*k)]

def print_graph(graph):
    ## 시간 초과 
    # for i in range(len(graph)):
    #     for j in range(len(graph[i])):
    #         print(graph[i][j], end='')
    #     print()
    for row in graph:
        print("".join(row))


def paint_star(x, y):
    for i in range(3):
        for j in range(5):
            graph[i+x][y+j] = min_tri[i][j]


def sol(k, x, y):
    if k == 1:
        paint_star(x, y)
        return
    
    sol(k//2, x, y+(3*k//2))
    sol(k//2, x+3*k//2, y)
    sol(k//2, x+3*k//2, y+3*k)

sol(k, 0, 0)
print_graph(graph)
