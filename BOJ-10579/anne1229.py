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
  copy_text = text[:]
  zeros_idx = []

  while '0' in copy_text:
    zero_idx = copy_text.index('0')
    num = copy_text[(zero_idx-1):(zero_idx+1)]
    zeros_idx.append(zero_idx - 1)
    copy_text = copy_text[:zero_idx-1] + copy_text[zero_idx+1:]

  for idx, t in enumerate(text):
    temp += t
    if idx in zeros_idx:
      continue
    if temp not in result:
      result.append(temp)
      temp = ''
  print(' '.join(list(result)))



