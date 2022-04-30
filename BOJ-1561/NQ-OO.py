import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
# n : 아이들의 수 
# m : 놀이기구 운행 시간 
rides_lst = list(map(int, input().rstrip().split()))

if m >= n : 
  sys.exit()

l, r = 0, 2000000000*30

# 모든 인원이 탑승하는데 걸리는 시간을 이분탐색으로 찾는다. 
mid = 0 
total_time = 0
while l <= r :
  mid = (l+r)//2
  cnt = m
  for rides_idx in range(m) : 
    cnt += (mid//rides_lst[rides_idx])
  if cnt >= n :
    total_time = mid
    r = mid - 1
  else : 
    l = mid + 1

#모든 인원이 놀이기구를 다 타기 1분 전에 몇명이 못 탔는지 계산 한다. 
cnt = m
for idx in range(m) : 
  cnt += (total_time-1) // rides_lst[idx]

#모든 인원이 놀이기구를 다 타는데 걸리는 시간에 딱 끝나는 놀이기구를 찾는다. 즉, 바로 직전에 비어있는 놀이기구를 찾아서 인원을 배치한다. 
vacant_rides = []
for idx in range(m) :
  if total_time % rides_lst[idx] == 0 : 
    vacant_rides.append(idx)


left_kid_cnt = n - cnt
print(vacant_rides[left_kid_cnt-1]+1)


  
  
  


