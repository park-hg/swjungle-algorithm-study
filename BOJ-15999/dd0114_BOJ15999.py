import sys

n, m = map(int,sys.stdin.readline().split())

box = []


for i in range(n):
    a = str(sys.stdin.readline().rstrip())
    box.append(a)

di = [1,0,-1,0]
dj = [0,1,0,-1]

cnt = 0

for i in range(n):
    for j in range(m):
        now = box[i][j]
        tmp = True
        for k in range(4):
            new_i = i+di[k]
            new_j = j+dj[k]
            if 0<= new_i <n and 0<= new_j <m:
                if now != box[new_i][new_j]:
                    tmp = False
                    break
        if tmp:
            cnt +=1

ans = 2**cnt % (10**9 +7)
print(ans)