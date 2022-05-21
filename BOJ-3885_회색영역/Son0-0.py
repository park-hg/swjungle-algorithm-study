# : (
import sys

input = sys.stdin.readline

def solution():
  while True:
    n, w = map(int, input().split())
    if n == 0 and w == 0 : return
    numlist = []
    for _ in range(n):
      numlist.append(int(input()))
      
    # 구간 수
    num_of_interval = (max(numlist) // w) + 1
    interval = [0 for _ in range(num_of_interval)]
    
    # max_value == 가장 높은 막대
    max_value = 0
    for num in numlist:
      idx = num // w
      interval[idx] += 1
      max_value = max(max_value, interval[idx])
    
    denominator = num_of_interval - 1
    ink = 0.01
    for idx, size in enumerate(interval):
      ink += (size / max_value) * ((denominator - idx) / denominator)
      
    print(ink)
    
solution()
