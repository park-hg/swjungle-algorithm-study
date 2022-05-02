from collections import Counter
def solution(N, stages):
    players = len(stages)
    counter = Counter(stages)
    answer = []
    for i in range(1, N+1):
        if i not in counter:
            answer.append((i, 0))
        else:
            answer.append((i, counter[i]/players))
            players -= counter[i]
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [a[0] for a in answer]
    return answer