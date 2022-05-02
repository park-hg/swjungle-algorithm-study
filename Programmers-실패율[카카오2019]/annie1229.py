def solution(N, stages):
    stop = [0 for _ in range(N+2)]
    total = len(stages)
    fail = [(0, 0) for _ in range(N+1)]
    result = []

    for stage in stages:
        stop[stage] += 1

    for i in range(1, N+1):
        if total <= 0:
            fail[i] = (0, i)
            continue
        fail[i] = (stop[i]/total, i)
        total -= stop[i]
    fail.sort(key=lambda x: (-x[0], x[1]))
    
    for f in fail:
        if f[1] == 0:
            continue
        result.append(f[1])
        
    return result

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
solution(4, [1, 2, 2, 2, 0])
solution(3, [1, 1, 1])