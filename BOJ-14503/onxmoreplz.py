import sys
import pprint

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]


N, M = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# pprint.pprint(arr)
arr[x][y] = 6

answer = 1
flag = True
# a = 5
while flag:
  # print(x, y, d)
  for temp_d in range(4):
    n_x = x + dir[(d - temp_d) % 4][0]
    n_y = y + dir[(d - temp_d) % 4][1]  
    
    if 0 <= n_x < N and 0 <= n_y < M:
      if arr[n_x][n_y] == 0:
        arr[n_x][n_y] = 2
        x, y = n_x, n_y
        answer += 1
        d = (d - temp_d - 1) % 4
        break
      else:
        if temp_d == 3:
          n_x = x + dir[(d + 3) % 4][0]
          n_y = y + dir[(d + 3) % 4][1]
          if arr[n_x][n_y] == 1:
            flag = False
          else:
            x = n_x
            y = n_y
        else:
          continue

print(answer)
# pprint.pprint(arr)
