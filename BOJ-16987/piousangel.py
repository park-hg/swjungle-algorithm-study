import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline


# 자신계란의 내구도는 상대 계란의 무게만큼 깎이게 된다. 
# 내구도가 0이하가 되는순간 계란을 깨진다 계란 2개다 깎임
# 가장왼쪽 계란부터 시작 -> 손에 든 계란이 깨졌거나 다른 계란이 다깨지면 넘어가
# 한칸 오른쪽 계란 들고 그 계란이 제일 오른쪽 계란일 때 종료


n = int(input())

egg_info = []

for i in range(n):
    a, b = map(int, input().split())
    egg_info.append([a,b])

print(egg_info)
visited = [False] * n
answer = 0

def dfs(egg_info, visited, idx, maxidx) :
    global answer
    print(idx, egg_info)

    if idx == maxidx:
        cnt = 0
        for egg in egg_info :
            if egg[0] <= 0 :
                cnt += 1
        answer = max(answer, cnt)
        return

    now_naegudo = egg_info[idx][0]
    now_weight = egg_info[idx][1]

    
    for i in range(len(egg_info)) :
        if i != idx and visited[i] != True and now_naegudo > 0 and egg_info[i][0] > 0 : # i번째 달걀의 내구도도 0보다 커야
            # print("rkrkrk가가가")
            # visited[i] = True

            now_naegudo -= egg_info[i][1]      #손에 들고있는 계란의 내구도 => 내구도 - 무게
            temp = egg_info[i][0] - now_weight       #옆에 손 계란의 내구도 => 내구도 - 무게
            
            # if now_naegudo <= 0 :
            #     visited[idx] = True
            # if temp <= 0 :
            #     visited[i] = True
   
            egg_info[idx] = [now_naegudo, now_weight]
            egg_info[i] = [temp, egg_info[i][1]]

            dfs(egg_info, visited, idx+1, maxidx)
            # visited[i] = False
            # visited[idx] = False
        elif i != idx and visited[i] != True and now_naegudo <= 0 or egg_info[i][0] <= 0 :
            # visited[i] = True
            dfs(egg_info, visited, idx+1, maxidx)
            # visited[i] = False

dfs(egg_info, visited, 0, n)
print(answer)


