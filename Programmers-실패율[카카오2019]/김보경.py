def solution(n, stages):
    stages.sort()
    result = []
    people = len(stages)

    for lev in range(1, n+1):
        if people == 0:
            result.append((0, lev))
            continue
        ing_people = stages.count(lev)
        fail = ing_people / people
        result.append((-fail, lev))
        people -= ing_people
    
    result.sort()
    return [r[1] for r in result]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
