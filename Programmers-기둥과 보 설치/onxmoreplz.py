import pprint

def solution(n, build_frame):
  wall = [[0] * (n + 1) for _ in range(n + 1)]

  answer = []
  for bf in build_frame:
    x, y, a, b = bf 
    if b == 1: # 설치
      if a == 0: # 기둥
        if y == 0  \
        or [x, y-1, 0] in answer  \
        or [x-1, y, 1] in answer  \
        or [x, y, 1] in answer:
          answer.append([x, y, 0])
      elif a == 1: # 보
        if [x, y-1, 0] in answer  \
        or [x+1, y-1, 0] in answer  \
        or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
          answer.append([x, y, 1])

        
    else: # 삭제
      if a == 0: # 기둥 
        if [x, y+1, 0] in answer:
          if [x-1, y+1, 1] not in answer and [x, y+1, 1] not in answer:
            continue
        if [x-1, y+1, 1] in answer:
          if [x-1, y, 0] not in answer \
          and ([x-2, y+1, 1] not in answer or [x, y+1, 1] not in answer):
            continue
        if [x, y+1, 1] in answer:
          if [x+1, y, 0] not in answer \
          and ([x-1, y+1, 1] not in answer or [x+1, y+1, 1] not in answer):
            continue
        answer.remove([x, y, 0])
            
      elif a == 1: #보
        if [x, y, 0] in answer:
          if [x, y-1, 0] not in answer and [x-1, y, 1] not in answer:
            continue
        if [x+1, y, 0] in answer:
          if [x+1, y-1, 0] not in answer and [x+1, y, 1] not in answer:
            continue
        if [x-1, y, 1] in answer:
          if [x-1, y-1, 0] not in answer and [x, y-1, 0] not in answer:
            continue
        if [x+1, y, 1] in answer:
          # 아래 둘다 기둥이 없다면
          if [x+1, y-1, 0] not in answer and [x+2, y-1, 0] not in answer:
            continue

        answer.remove([x, y, 1])

  
  return sorted(answer, key = lambda x : (x[0], x[1], x[2]))



# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
