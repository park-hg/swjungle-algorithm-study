## [1번] (백준 1897번) 토달기
## 혜진 센세 답안 복붙....

import sys

D, origin = sys.stdin.readline().split()
dictionary = sorted([sys.stdin.readline().strip() for _ in range(int(D))], key = lambda x : len(x))

answer = origin
possible = {origin : 1}
for word in dictionary:
  temp_length = len(word)
  for i in range(temp_length):
    temp_word = word[:i] + word[i+1:]
    if temp_word in possible:
      possible[word] = 1
      if len(word) > len(answer):
        answer = word


print(answer)
