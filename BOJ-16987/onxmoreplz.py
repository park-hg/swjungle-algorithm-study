# 중복조합으로 풀어보려 했지만
# 아쉽게도 장렬히 전사하였습니다.

import sys
from itertools import product
import copy

N = int(sys.stdin.readline().strip())
eggs = []
for _ in range(N):
  eggs.append(list(map(int, sys.stdin.readline().split())) + [True])
num = [X for X in range(N)]

# print(eggs, num)
numbers = []
for i in range(N):
  numbers.append(num[:i] + num[i+1:])


answer = 0
for pro in product(num, repeat = N):
  # print(pro)
  temp_answer = 0
  temp_eggs = copy.deepcopy(eggs)
  for i in range(N):
    if i == pro[i]:
      break
    if temp_eggs[i][2] and temp_eggs[pro[i]][2]:  
      if temp_eggs[i][0] - temp_eggs[pro[i]][1] <= 0:
        temp_eggs[i][2] = False
        temp_answer += 1
        # print('-->', i, pro[i])
      else:
        temp_eggs[i][0] -= temp_eggs[pro[i]][1]
      if temp_eggs[pro[i]][0] - temp_eggs[i][1] <= 0:
        temp_eggs[pro[i]][2] = False
        temp_answer += 1
        # print('--->', i, pro[i])
      else:
        temp_eggs[pro[i]][0] -= temp_eggs[i][1]      

  answer = max(answer, temp_answer)
      
print(answer)
