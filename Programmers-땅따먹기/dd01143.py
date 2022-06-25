def solution(land):
    answer = 0
    length = len(land)
    for i in range(1,length):
        for j in range(4):
            tmp = 0
            for k in range(4):
                if j == k:
                    continue
                tmp = max(tmp,land[i-1][k])
            land[i][j] += tmp
    
    answer = max(land[-1])


    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))