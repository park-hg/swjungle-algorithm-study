import heapq

def solution(info, edges):
  graph = [[] for _ in range(len(info))]
  for edge in edges:
    graph[edge[0]].append(edge[1])

  print(graph)
  
  answer = 0
  heap = [(0, 0, 0)] #([양|늑대] 구분, 양을 가진 자식노드 개수, 현재 노드 번호)
  visited = []
  sheep_count = 0
  
  while heap:
    animal, child_sheep_cnt, curr = heapq.heappop(heap)
    print('-->', curr, heap)
    if info[curr] == 1 and sheep_count - 1 <= 0:
      continue
    elif info[curr] == 1:
      sheep_count -= 1
      
    if curr not in visited:
      sheep_count += abs(animal - 1)
      answer += abs(animal - 1)
      
    
    for next in graph[curr]:
      if info[next] == 0: # 다음노드가 양인 경우
        heapq.heappush(heap, (0, 0, next))
      else: # 다음노드가 늑대인 경우
        if not graph[next]: # 마지막 노드인 경우
          continue
        temp_sheep_cnt = 0
        for next_next in graph[next]: # 다음 노드 기준 양 개수 
          temp_sheep_cnt += abs(info[next_next] - 1)
        heapq.heappush(heap, (1, -temp_sheep_cnt, next))
  

  print(answer)
  return answer
