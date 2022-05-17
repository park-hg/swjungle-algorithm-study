import sys

n, m = map(int,sys.stdin.readline().split())

box = []
coin = []
visit = []

for i in range(n):
    a= sys.stdin.readline().rstrip()
    box.append(a)
    visit.append(a)

    for j in range(m):
        if a[j] == 'o':
            coin.append([i,j])

l = [1,0,-1,0]
r = [0,1,0,-1]

q = [[coin[0],coin[1],0]]
ans = 500

while q :
    c1,c2,count = q.pop()
    count +=1

    if count >= ans :
        break

    for d in range(4):
        # 움직인다.
        # 벽으로 움직이는지 떨어졌는지 확인
        # 둘다 떨어지면 pass. 하나만떨어지면 성공 카운트 등록 
        # 둘다 안떨어지면 큐에 전달
        drop =0
        new_c1_l = c1[0]+l[d]
        new_c1_r = c2[1]+r[d]
        new_c2_l = c2[0]+l[d]
        new_c2_r = c2[1]+r[d]

        new_c1 = [new_c1_l,new_c1_r]
        new_c2 = [new_c2_l,new_c2_r]

        if 0<= new_c1_l < n and 0<= new_c1_r < m :
            if box[new_c1_l][new_c1_r] == '#':
                new_c1 = c1   
        else :
            drop +=1

        if 0<= new_c2_l < n and 0<= new_c2_r < m :
            if box[new_c2_l][new_c2_r] == '#':
                new_c2 = c2   
        else :
            drop +=1

        if drop == 2 :
            continue
        elif c1 == new_c1 and c2 == new_c2:
            continue
        elif new_c1 == new_c2:
            continue
        elif drop == 1:
            ans = min(ans,count)
        else:
            q.append([new_c1,new_c2,count])

if ans == 500:
    print(-1)
else :
    print(ans)