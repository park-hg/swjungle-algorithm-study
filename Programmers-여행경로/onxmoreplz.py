def solution(tickets):
  
  def dfs(curr, _route, visited):
    global flag, answer
    if len(visited) == ticket_cnt + 1:
      answer = visited[:]
      flag = True
      return
  
    if curr in _route and not flag:
      for i in range(len(_route[curr])):
        if not _route[curr][i][1]:
          _route[curr][i][1] = True
          visited.append(_route[curr][i][0])
          dfs(_route[curr][i][0], _route, visited)
          _route[curr][i][1] = False
          visited.pop()

  
  tickets.sort(key = lambda x : x[1])
  route = {}
  ticket_cnt = 0
  for a, b in tickets:
    if a not in route:
      route[a] = [[b, False]]
    else:
      route[a].append([b, False])
    ticket_cnt += 1

  global flag
  flag = False
  
  dfs("ICN", route, ["ICN"])

  print(answer)
  return answer
