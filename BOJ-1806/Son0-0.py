# 10 15
# 5 1 3 5 10 7 4 9 2 8

# 5 6 

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

def solution():
  answer = sys.maxsize
  
  if N == 0:
    print('0')
    return
  elif N == 1:
    if N == S:
      print('1')
      return
    else: print('0')
    
    
  left, right = 0, 1
  num = nums[left]
  while left < right and right < N:
    num += nums[right]
    if num < S:
      right += 1
    else:
      while S < num:
        num -= nums[left]
        left -= 1
        # print(num, answer)
        answer = min(answer, right - left)
      right += 1
      left += 1
      # print(left, right)
  
  print(answer)
        
    
  
  # for i in range(N):
  #   ptr, num = i, 0
  #   while ptr < N:
  #     num += nums[ptr]
  #     ptr += 1
  #     if S <= num:
  #       # print('num: ', num)
  #       # print('length: ', ptr - i)
  #       answer = min(answer, ptr - i)
  #       break
      
  # if answer == sys.maxsize:
  #   print('0')
  # else:      
  #   print(answer)
  
solution()
  
