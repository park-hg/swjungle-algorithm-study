import sys

n = int(input())

eggs = []

for _ in range(n):
    hp,attack = map(int,sys.stdin.readline().split())
    eggs.append((hp,attack))

q = []
# 부신횟수, 현재 계란, 부셔야할 계란들
for i in range(n):
    broken = 0
    now = (eggs[i][0],eggs[i][1])
    remain = []
    for j in range(n):
        if j != i :
            remain.append(j)

    count = n-1
    q.append([broken, now, remain, count])

ans = 0

while q :
    if count == 0 :
        continue

    elif ans >= count+broken:
        continue

    else:
        broken, now, remain, count = q.pop()
        
        for i in remain:
            next = eggs[i]
            new_remain = []
            for j in remain:
                if j == i:
                    continue
                else:
                    new_remain.append(j)

            if now[0] - next[1] <= 0:
                broken += 1
                ans = max(ans,broken)

            new_hp = next[0] - now[1]
            
            if new_hp >0 :
                now = (new_hp,now[1])
                count -= 1
                new_q = [broken,now,new_remain,count]
                q.append(new_q)

            else :
                for k in new_remain:
                    now = eggs[k]
                    new_new_remain =[]
                    broken += 1
                    ans = max(ans,broken)

                    for l in new_remain:
                        if l == k :
                            continue
                        else:
                            new_new_remain.append(l)
                            new_q = [broken,now,new_new_remain,count-1]
                            q.append(new_q)

print(ans)