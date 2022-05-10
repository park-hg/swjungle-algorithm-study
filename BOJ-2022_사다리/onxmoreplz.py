import sys
import math

x, y, c = map(float, sys.stdin.readline().split())
left = 0
right = min(x, y)

answer = 0
while right - left > 10**(-6):
  mid = (left + right) / 2

  x_height = math.sqrt(x*x - mid*mid)
  y_height = math.sqrt(y*y - mid*mid)
  
  if x_height * y_height / (x_height + y_height) >= c:
    answer = mid
    left = mid
  else:
    right = mid

print(answer)
