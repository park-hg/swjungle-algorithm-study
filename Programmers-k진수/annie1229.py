
def change_number(num, k):
  result = ''
  while num:
    result = str(num % k) + result
    num //= k
  return result

def solution(n, k):
    answer = 0
    ch_num = change_number(n, k)

    nums = []
    temp = ''
    for ch in ch_num:
      if ch != '0':
        temp += ch
      else:
        if temp:
          nums.append(int(temp))
          temp = ''
    if temp:
      nums.append(int(temp))

    max_num = max(nums)
    is_prime = [False for _ in range(max_num + 1)]
    is_prime[2] = True
    primes = set([2])
    for i in range(3, max_num + 1):
      if i % 2:
        if not is_prime[i]:
          primes.add(i)
          for ii in range(i, max_num + 1, i):
            is_prime[ii] = True

    for num in nums:
      if num in primes:
        answer += 1
    print(answer)
    return answer

solution(437674, 3)
solution(110011, 10)