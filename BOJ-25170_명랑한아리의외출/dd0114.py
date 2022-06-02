import sys

n, m, t = map(int,sys.stdin.readline().split())

works = []
spend = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    works.append(a)

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    spend.append(a)

max_work = [[[0]*m for _ in range(n)] for _ in range(t+1)]

q = [(0,0,0,0)]
answer = 0

dn = [1,0,1]
dm = [0,1,1]

while q :
    now_n, now_m, now_w,now_t = q.pop()

    for i in range(3):
        for j in range(2):
            next_n = now_n+dn[i]
            next_m = now_m+dm[i]

            if next_n < n and next_m < m:
                next_w = now_w+ j*works[next_n][next_m]
                next_t = now_t+1+ j*spend[next_n][next_m]
                if next_t > t:
                    continue

                if next_w > max_work[next_t][next_n][next_m] and next_w > max_work[next_t-1][next_n][next_m]:
                    max_work[next_t][next_n][next_m] = next_w
                    q.append((next_n, next_m, next_w, next_t))
                    same_nm = next_t+1
                    while True :
                        if same_nm >t :
                                break
                        if next_w > max_work[same_nm][next_n][next_m]:
                            max_work[same_nm][next_n][next_m] = next_w 
                            same_nm += 1
                        else :
                            break


answer = max_work[i][-1][-1]

print(answer)