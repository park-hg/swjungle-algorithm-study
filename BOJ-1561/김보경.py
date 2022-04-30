## 보고 풀었습니다 
#2.46
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

start = 0
end = N * 30

rides = list(map(int, input().rstrip().split()))

ans_time = None

if M >= N:
    print(N)
else:
    while start <= end:
        mid = (start + end) // 2

        cnt = M
        for i, ride in enumerate(rides):
            cnt += mid // ride 

        if cnt >= N:
            ans_time = mid
            end = mid -1
        else:
            start = mid + 1

    cnt = M
    for i, ride in enumerate(rides):
        cnt += (ans_time-1) // ride 

    for i, ride in enumerate(rides):
        if not ans_time % ride:
            cnt += 1

        if cnt == N:
            print(i+1)
            break

