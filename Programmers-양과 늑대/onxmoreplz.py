def solution(info, edges):
  graph = [[] for _ in range(len(info))]
  for edge in edges:
    graph[edge[0]].append(edge[1])

  print(graph)
  
  answer = 0
  stack = [(1, 0, [0])] #([양 개수, 늑대 개수, 현재 노드 번호)
  
  while stack:
    sheep_cnt, wolf_cnt, visited = stack.pop()
    print(visited)
    answer = max(answer, sheep_cnt)
      
    for curr in visited:
      for next in graph[curr]:
        if next not in visited:
          next_sheep_cnt = sheep_cnt
          next_wolf_cnt = wolf_cnt
          if info[next]:
            next_wolf_cnt += 1
          else:
            next_sheep_cnt += 1
          if next_sheep_cnt <= next_wolf_cnt:
            continue
          stack.append((next_sheep_cnt, next_wolf_cnt,visited + [next]))
  

  print(answer)
  return answer
