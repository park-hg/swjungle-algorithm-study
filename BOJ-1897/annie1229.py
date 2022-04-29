# 1. 토달기(#1897)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, start = input().rstrip().split()

dictionary = []
for _ in range(int(N)):
    dictionary.append(input().rstrip())
dictionary.sort(key=lambda x: len(x)) # 단어들 길이 오름차순 정렬

result = start # 선생님이 말한 단어를 result 초깃값으로 설정
memo = { start: 1 } # 단어들 저장해둘 dict
for text in dictionary: # 짧은 단어들부터 for문 돌기
    n = len(text)
    for k in range(0, n): # 단어의 첫인덱스부터 끝-1인덱스까지 돌면서
        newText = text[0:k] + text[k+1:n] # k번째 자리 없는 단어 만들기
        if newText in memo: # 그 단어가 이전에 만들었던 단어중에 있으면
            memo[text] = 1 # 현재 단어도 dict에 추가
            if len(text) > len(result): # result보다 더 긴 단어면 result 갱신
                result = text
print(result)
