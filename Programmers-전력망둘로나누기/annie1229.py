check_dict = {}
def dfs(n, graph, visited, check):
  if not visited[n]:
    visited[n] = True
    for i in graph[n]:
      if (n, i) in check_dict:
        if not check[check_dict[(n, i)]]:
          dfs(i, graph, visited, check)
      elif (i, n) in check_dict:
        if not check[check_dict[(i, n)]]:
          dfs(i, graph, visited, check)

def solution(n, wires):
    # 1개를 끊어서 최대한 비슷한 개수로 나누기
    answer = -1
    wire_graph = [[] for _ in range(n + 1)]
    for idx, wire in enumerate(wires):
      a, b = wire
      wire_graph[a].append(b)
      wire_graph[b].append(a)
      check_dict[(a, b)] = idx
      
    check = [False for _ in range(len(wires))]
    min_diff = n
    min_cnt = 0
    for idx, wire in enumerate(wires):
      visited = [False for _ in range(n + 1)]
      check = [False for _ in range(len(wires))]
      check[idx] = True
      dfs(1, wire_graph, visited, check)
      print(idx, wire, visited.count(True))
      true_cnt = visited.count(True)
      false_cnt = visited.count(False)
      diff = abs(true_cnt - false_cnt)
      if diff < min_diff:
        min_diff = diff
        min_cnt = true_cnt
    print('min diff', min_diff, min_cnt)
    a = n - min_cnt;
    answer = abs(min_cnt - a)
    print('ans',answer)
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(4, [[1,2],[2,3],[3,4]])
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])