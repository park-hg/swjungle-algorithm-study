# 순열 장난(BOJ-10579) 틀렸습니다..
import sys
sys.stdin = open('input.txt')

text = sys.stdin.readline().rstrip()
result = []
temp = ''

if len(text) < 10:
  result = list(text)
  print(' '.join(result))
else:
  max_num = (len(text) - 9) // 2 + 9
  copy_text = text[:]
  zeros_idx = []

  while '0' in copy_text:
    zero_idx = copy_text.index('0')
    zeros_idx.append(zero_idx - 1 + len(zeros_idx) * 2)
    copy_text = copy_text[:zero_idx-1] + copy_text[zero_idx+1:]

  for idx, t in enumerate(text):
    temp += t
    if idx in zeros_idx:
      continue
    if idx + 1 < len(text):
      if int(temp + text[idx+1]) <= max_num and (temp + text[idx+1]) not in result:
        continue
    if temp not in result:
      result.append(temp)
      temp = ''
  print(' '.join(list(result)))



