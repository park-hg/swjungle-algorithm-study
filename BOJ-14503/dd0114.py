import sys

n, m = map(int,sys.stdin.readline().split())
s, g, d = map(int,sys.stdin.readline().split())

box = []
check = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    check.append(a)
    box.append(a)

direct = d
count = 0
rotate = 0

dl = [0,-1,0,1]
dr = [-1,0,1,0]

q = (s, g)

while q :
    l,r = q
    if check[l][r] == 0:
        check[l][r] = 1
        count += 1

    new_l = l+dl[d]
    new_r = r+dr[d]
    new_d = (d-1)%4

    if check[new_l][new_r] == 0:
        d = new_d
        rotate = 0
        q = (new_l,new_r)

    else :
        rotate += 1
        d = new_d
        if rotate ==4:
            back_d = (d-1)%4
            back_l = l+dl[back_d]
            back_r = r+dr[back_d]
            if box[back_l][back_r] == 1:
                q = False
                break
            q = (back_l,back_r)
            rotate = 0

print(count)




# print(count)