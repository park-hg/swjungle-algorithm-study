def solution(n, s):  
  answer = []
  temp_s = s
  temp_n = n
  
  while len(answer) < n - 1:
    x = temp_s // temp_n
    if x == 0:
      break

    if temp_s % temp_n == 0:
      print(temp_s // temp_n)
      answer += [x] * temp_n
      break
    else:
      answer.append(x)
      
      temp_s -= x
      temp_n -= 1
    

  answer.append(temp_s)
  # print(answer)
  
  if len (answer) == n:
    return answer
  elif len(answer) >= n:
    answer.pop()
    return answer
  else:
    answer = [-1]
  # print(answer)
  return answer
