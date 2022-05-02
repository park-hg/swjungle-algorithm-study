# https://programmers.co.kr/learn/courses/30/lessons/42889

from collections import deque

def solution(N, stages):
    stage_size = len(stages)
    stages = deque(sorted(stages))

    result = []
    for idx in range(1, N + 1):
        cnt = 0
        while stages and stages[0] == idx:
            stages.popleft()
            cnt += 1
        if stage_size == 0:
          result.append((idx, 0))
        else:
          result.append((idx, cnt / stage_size))
        stage_size -= cnt
        
        
    return list(stage[0] for stage in sorted(result, reverse=True, key=lambda x: x[1]))
