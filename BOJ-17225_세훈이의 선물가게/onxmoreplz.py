import sys

A, B, N = map(int, sys.stdin.readline().split())
sang_last, ji_last = 0, 0
order = []

for _ in range(N):
  time, color, cnt = list(sys.stdin.readline().split())
  time = int(time)
  cnt = int(cnt)
  
  if color == 'B':
    for i in range(cnt):
      if sang_last > time:
        time = sang_last
      order.append((time + A*i, color))
    sang_last = time + A * cnt
  else:
    for i in range(cnt):
      if ji_last > time:
        time = ji_last
      order.append((time + B*i, color))
    ji_last = time + B * cnt

order.sort(key = lambda x: (x[0], x[1]))

sangmin = []
jisu = []
nums = 1
while order:
  if order[0][1] == 'B':
    sangmin.append(nums)
  else:
    jisu.append(nums)
  nums += 1
  del order[0]

print(len(sangmin))
print(*sangmin, sep = ' ')
print(len(jisu))
print(*jisu, sep = ' ')
  
