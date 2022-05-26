#시간초과 
import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline


#첫줄에 길이 N짜리 수열, 부분합이 S 이상된다?

n, s = map(int, input().split())

n_list = list(map(int, input().split()))

idx = 0
temp_idx = 0
temp_list = []
total = 0
answer = 100000
while True:

    if temp_idx == len(n_list):
        break

    total += n_list[temp_idx]

    if total >= s :
        n_len = idx - temp_idx 
        answer = min(answer, n_len)
        temp_idx +=1       #하나씩 가게
        idx = temp_idx
        total = 0

    idx += 1

if answer == 100000 :
    print("0")
else :   
    print(answer)