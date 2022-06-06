import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [S]
for volume in volumes:
  temp = set()
  for vol in dp:
    lg_vol = vol + volume
    sm_vol = vol - volume
    if 0 <= sm_vol <= M:
      temp.add(sm_vol)
    if 0 <= lg_vol <= M:
      temp.add(lg_vol)
  dp = temp

if len(dp) == 0:
  print(-1)
else:
  print(max(dp))

