# 형규님것 보고 다시 풀었습니다
def solution(info, edges):
    def dfs(visited, visited_g, wolf, sheep):
        nonlocal ans
        ans = max(ans, sheep)
        for v in range(N):
            if (1<<v) & visited:
                for des in graph[v]:
                    if not ((1<<des) & visited):
                        new_visited = visited | (1<<des)
                        if visited_g[new_visited] : continue
                        visited_g[new_visited] = True
                        if info[des]:
                            if wolf+1 < sheep:
                                dfs(new_visited, visited_g, wolf+1, sheep)
                        else:
                            dfs(new_visited, visited_g, wolf, sheep+1)

    N = len(info)
    graph = [[] for _ in range(N)]
    for x, y in edges:
        graph[x].append(y)
    
    ans = 1
    visited_g = [False] * (1<<N)
    dfs(1, visited_g, 0, 1)
    return ans

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
print(solution([0,0,0,1,0], [[0,1],[0,2], [2,3], [3,4]]))
