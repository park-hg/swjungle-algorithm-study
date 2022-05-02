from collections import deque

def solution(N, stages):
    answer = []
    stages_success_rate = []
    total_gamer_cnt = len(stages)
    stage_gamer_cnt = total_gamer_cnt
    stages.sort()
    stage_q = deque(stages)
    for stage_idx in range(1, N+1) : 
      cnt = 0
      while (len(stage_q) > 0) and (stage_q[0] == stage_idx)  : 
        cnt += 1
        stage_q.popleft()
      print(cnt)
      if cnt != 0 : 
        stages_success_rate.append([stage_idx, cnt/stage_gamer_cnt])
      else : 
        stages_success_rate.append([stage_idx, 0])
      stage_gamer_cnt -= cnt
    stages_success_rate.sort(reverse=True, key= lambda x: (x[1], -x[0]))
    answer = [ idx[0] for idx in stages_success_rate ]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(3, [1,1,1]))
