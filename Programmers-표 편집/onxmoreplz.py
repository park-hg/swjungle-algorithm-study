def solution(n, k, cmd):
  table = [X for X in range(n)]
  # print(table)
  stack = []
  
  for c in cmd:
    if c[0] == 'U':
      if k - int(c[2]) < 0:
        k = 0
      else:
        k -= int(c[2])
    elif c[0] == 'D':
      if k + int(c[2]) >= len(table) - 1:
        k = len(table) - 1
      else:
        k += int(c[2])
    elif c[0] == 'C':
      stack.append(table[k])
      del table[k]
      if k == len(table):
        k -= 1
    else: # 'Z'
      popped = stack.pop()
      if popped < table[k]:
        k += 1
      table.append(popped)
      table.sort()

    print(c, '-->', table, stack, k)

    
  # 출력
  answer = ""
  for i in range(n):
    if i in stack:
      answer += 'X'
    else:
      answer += 'O'

  # print(answer)
  return answer



solution(8, 2, ["D 2","C","C","C","C","C", "Z", "Z", "U 2", "C"])
# solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
