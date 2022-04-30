# 2. 놀이 공원(#1561)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split()) # N: N명의 아이들, M: M개의 1인승 놀이기구
time = list(map(int, input().split())) # 놀이기구별 운행 시간
minT = min(time) # 놀이기구 최소 운행 시간
maxT = max(time) * N # 놀이기구 최대 운행 시간

if N <= M: # 아이들이 놀이기구 수 보다 적으면 N그대로 출력
    print(N)
    exit(0)
N -= M # 처음에는 M개의 놀이기구에 아이들이 다같이 타니까 태워야하는 총 N명에서 빼주기

def check(s, e): # N명(=아직 못탄 아이들)이 놀이기구 다 타는데 걸리는데 몇분 걸리는지
    res = 0
    while s <= e: # 이분탐색 종료조건
        mid = (s + e) // 2 
        total = 0 # mid분동안 놀이기구 탈 수 있는 총 인원수 저장할 변수
        for t in time:
            total += mid // t # mid분동안 운행 시간 t인 놀이기구에 몇명이 탈 수 있는지 구해서 total에 더하기
        if total >= N: # 태워야할 아이들 다 태웠으면
            e = mid - 1 # 놀이기구 총 운행 시간 줄여서 다시 이분탐색하도록
            res = mid # 아이들 다 태웠을때 걸리는 시간 res에 저장(이분 탐색 진행하면서 점점 최소 시간에 가까워짐)
        else:
            s = mid + 1 # 아직 다 못태웠으면 놀이기구 총 운행 시간 늘여서 다시 이분탐색하도록
    return res # 아이들 다 태우는데 걸리는 최소시간 반환

result = check(minT, maxT) # result: 아이들 다 태우는데 걸리는 최소시간
total = 0 # 아이들 다 태우기 1분전까지 탄 총 인원수 담을 변수
for t in time:
    total += ((result - 1) // t) # result - 1분까지 운행 시간 t인 놀이기구에 타는 인원수 구해서 total에 더하기
k = N - total # 아직 못탄 인원수 - (result-1)분까지 탄 인원수 빼면 result분일 때 몇명(k) 더 태워야하는지 알 수 있음
div = [] # result분에 비어있는 놀이기구들 담을 배열
for idx, i in enumerate(time):
    if result % i == 0: # result분에 비어있는 놀이기구면
        div.append(idx + 1) # div 배열에 놀이기구 번호(인덱스+1) 추가
print(div[k - 1]) # 마지막 사람이 타는 놀이기구 번호 출력
# div[k-1]은 div배열 인덱스가 0부터 시작하니까 k-1해주는거
    