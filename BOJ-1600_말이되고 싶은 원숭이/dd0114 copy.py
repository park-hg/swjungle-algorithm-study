import sys

k = int(input())
w,h = map(int,sys.stdin.readline().split())
answer = w*h+1
box =[]

for i in range(h):
    a = list(map(int,sys.stdin.readline().split()))
    box.append(a)

max_time = (w*h)+1

dp = [[([max_time]*w) for _ in range(h)] for _ in range(k+1)]

q = [(0,0,0,0)]

w_l = [1,0,-1,0]
w_r = [0,1,0,-1]
h_l = [2,1,2,-1,-2,1,-1,-2]
h_r = [1,2,-1,2,1,-2,-2,-1]

while q:
    n_h,n_w,spend_k,time = q.pop()
    time +=1
    if time >= answer:
        continue

    for i in range(4):
        new_h = n_h+w_l[i]
        new_w = n_w+w_r[i]
        if 0<= new_h < h and 0<= new_w <w and box[new_h][new_w] == 0:
            old = dp[spend_k][new_h][new_w]
            if time < old :
                dp[spend_k][new_h][new_w] = time
                q.append((new_h,new_w,spend_k,time))
                if new_h == h-1 and new_w == w-1:
                    answer = min(answer,time)

    if spend_k < k:
        spend_k +=1
        for i in range(8):
            new_h = n_h+h_l[i]
            new_w = n_w+h_r[i]
            if 0<= new_h < h and 0<= new_w <w and box[new_h][new_w] == 0:
                old = dp[spend_k][new_h][new_w] 
                if time < old :
                    dp[spend_k][new_h][new_w] = time
                    q.append((new_h,new_w,spend_k,time))
                    if new_h == h-1 and new_w == w-1:
                        answer = min(answer,time)


# for i in range(k+1):
#     answer = min(answer,dp[i][-1][-1])

if answer == max_time:
    print(-1)
else :
    print(answer)

# print(answer)