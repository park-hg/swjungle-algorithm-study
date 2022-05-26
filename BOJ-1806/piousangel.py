import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, s = map(int, input().split())

n_list = list(map(int, input().split()))
answer = 1000000001
def search(n_list, s) :
    global answer
    q = deque()
    
    q.append(n_list[0])
    idx = 0
    total = n_list[0]

    while q :
        if idx == len(n_list)-1:
            while len(q) >= 1 :  #마지막 인덱스까지 왔으면 앞에거 빼주면서 s보다 큰거 있는지 chk 
                temp = q.popleft()
                total -= temp
                if total >= s :
                    answer = min(answer, len(q))
            break

        if total < s :
            idx += 1
            total += n_list[idx]
            q.append(n_list[idx])
        else:
            answer = min(answer, len(q))
            temp = q.popleft()
            total -= temp

search(n_list, s)

if answer == 1000000001 :
    print(0)
else:
    print(answer)



# #시간초과 
# import sys
# sys.stdin = open('sample.txt')
# input = sys.stdin.readline


# #첫줄에 길이 N짜리 수열, 부분합이 S 이상된다?

# n, s = map(int, input().split())

# n_list = list(map(int, input().split()))

# idx = 0
# temp_idx = 0
# temp_list = []
# total = 0
# answer = 100000
# while True:

#     if temp_idx == len(n_list):
#         break
    
#     if total > answer :
#         continue

#     total += n_list[temp_idx]

#     if total >= s :
#         n_len = idx - temp_idx 
#         answer = min(answer, n_len)
#         temp_idx +=1       #하나씩 가게
#         idx = temp_idx     
#         total = 0

#     idx += 1

# if answer == 100000 :
#     print("0")
# else :   
#     print(answer)