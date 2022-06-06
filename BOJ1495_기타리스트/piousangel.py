import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨
# 현재 볼륨이 P이고 i번째곡을 연주하기 전이라면 i번째 곡은 P+V[i] or P - V[i]로 연주 가능
# 0보다 작을 수 없고 M보다 클수 없다
# N은 곡의 개수, S는 시작 볼륨, M은 최대 볼륨, 둘째줄에는 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이
# 시간초과

n, s, m = map(int, input().split())
n_list = list(map(int, input().split()))

def dfs(n_list, now, maxVol, idx) :
    global answer
    if idx == len(n_list) :
        answer = max(answer, now)
        return
    
    if now + n_list[idx] <= maxVol :
        dfs(n_list, now + n_list[idx], maxVol, idx+1)
    if 0 <= now - n_list[idx] :
        dfs(n_list, now - n_list[idx], maxVol, idx+1)
    else:
        return
answer = -1
dfs(n_list, s, m, 0)
print(answer)
