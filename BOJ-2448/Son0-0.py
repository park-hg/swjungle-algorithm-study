# 너무 어려워요 : (
# 풀어보는 중
# https://www.acmicpc.net/problem/2448

import sys

input = sys.stdin.readline

N = int(input())
floor_length = N // 3

square = [1, 2, 4, 8, 16, 64, 128, 256, 512, 1024]
slist = ['   ', '  *  ', ' * * ', '***** ']

def make_start(floor):
  if floor == floor_length:
    return
  
  temp = ''
  if not (floor + 1) in square:
    for i in range(floor - 1):
      temp += slist[0]
    
  for i in range(1, 4):
    pt = ''
    for j in range(floor + 1):
      if floor in square:
        if j == 1:
          pt += slist[i]
          continue
        pt += slist[i] + temp
      else:
        if j == 1:
          pt += temp
          continue
        pt += temp + slist[i]
          
    print(pt, end='')
    print("")
    
  make_start(floor + 1)

def solution():
  make_start(0)
  
  return

solution()
