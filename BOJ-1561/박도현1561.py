import sys
n, m = map(int,sys.stdin.readline().split())
gigu = list(map(int,sys.stdin.readline().split()))
saram = 1
time = 0
now = 0
while saram != n+1 :
    for i in range(m):
        if time % gigu[i] ==0 :
            saram +=1
            now = i+1
            if saram == n+1:
                break
    time +=1

print(now)