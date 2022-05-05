import sys
from tracemalloc import start
input = sys.stdin.readline

def possible(mid, c) : 
  cnt = 0
  for onion_len in len_lst : 
    cnt += onion_len//mid
  if cnt >= c : 
    return True
  return False

s, c = map(int, input().split())
len_lst = [int(input()) for _ in range(s)]

l = 1 
r = max(len_lst)
while l <= r : 
  mid = (l+r)//2
  if possible(mid, c) : 
    l = mid + 1
    max_len = mid
  else : 
    r = mid - 1

left_onion = sum(len_lst) - max_len*c
print(left_onion)
    
    
    