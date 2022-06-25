# 총 4열로 이뤄져있음
# 행은 10만개 이하
# 바로 위행과 같은 열을 밟을 수 없음

def solution(land):
    answer = 0
    
    for i in range(0, len(land) - 1) :
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    
    #print(land)
    
    answer = max(land[-1])
    
    return answer