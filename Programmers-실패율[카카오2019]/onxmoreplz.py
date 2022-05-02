from collections import Counter

def solution(N, stages):

  complete = [0] * (N)
  counter = Counter(stages)

  # Stage별 진행한 사람들 세기
  for i in range(len(stages)):
    for j in range(stages[i]):
      if j == N:
        break
      complete[j] += 1

  # Stage별 실패율 구하기
  failure = []
  for stage_number, on_stage in enumerate(complete):
    if on_stage != 0:
      failure.append((stage_number + 1, counter[stage_number+1] / on_stage))
    else:
      failure.append((stage_number + 1, 0))

  failure.sort(key = lambda x : x[1], reverse = True)
  
  # 출력하기
  answer = []
  for i in range(len(failure)):
    answer.append(failure[i][0])
  return answer

# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# solution(4, [4,4,4,4,4])
solution(4, [2,2,2,2,1]) # 런타임 에러 반례(zero division)
# solution(2, [1, 2])
