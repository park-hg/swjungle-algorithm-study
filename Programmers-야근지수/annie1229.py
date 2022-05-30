# Programmers 야근 지수 https://programmers.co.kr/learn/courses/30/lessons/12927
def calc(arr):
  total = 0
  for a in arr:
    total += a**2
  return total

def solution(n, works):
    answer = 0
    total_time = sum(works)
    after_time = total_time - n

    if after_time <= 0:
      return 0

    div_time = after_time // len(works) # 남은 시간을 균등분배했을 때 시간
    remain = after_time % len(works) # 더 일해야하는 시간(나머지)
    new_arr = []

    for work in works:
      if div_time <= work:
        new_arr.append(div_time)
      else:
        new_arr.append(work)
        remain += (div_time - work)

    for i in range(1, remain + 1):
      new_arr[i % len(works)] += 1
    
    answer = calc(new_arr)
    print('div', div_time, 'remain', remain, 'newarr', new_arr, 'ans >> ',answer)
    return answer

solution(4, [4, 3, 3])
solution(1, [2, 1, 2])
solution(3, [1,1])
print(calc([2,2,2]))