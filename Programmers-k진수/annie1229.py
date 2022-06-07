
def change_number(num, k):
  result = ''
  while num:
    result = str(num % k) + result
    num //= k
  return result

def is_prime(num):
  if num == 1:
    return False
  for n in range(2, int(num**0.5)+1):
    if num % n == 0:
      return False
  return True

def solution(n, k):
    answer = 0
    ch_num = change_number(n, k)

    temp = ''
    for ch in ch_num:
      if ch != '0':
        temp += ch
      else:
        if temp:
          if is_prime(int(temp)):
            answer += 1
          temp = ''
    if temp:
      if is_prime(int(temp)):
            answer += 1

    print(answer)
    return answer

solution(437674, 3)
solution(110011, 10)