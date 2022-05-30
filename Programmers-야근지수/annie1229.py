# Programmers 야근 지수 https://programmers.co.kr/learn/courses/30/lessons/12927
def calc(arr):
  total = 0
  for a in arr:
    total += a**2
  return total

def solution(n, works):
    if sum(works) <= n:
      return 0
    while n:
      works.sort(reverse=True)
      max_num = max(works)
      for i in range(len(works)):
        if works[i] == 0: continue
        if n == 0: break
        if max_num <= works[i]:
          works[i] -= 1
          n -= 1
    return calc(works)