import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, str1 = map(str, input().split())
str_list = []

for i in range(int(n)):
    str_list.append(input().rstrip())       #사전에 등재된 단어만 사용가능

str_list.sort(key = len)
# print(str_list)

dic = []
dic.append(str1)      #기본 추가

for strs in str_list:
    
    if strs in dic :
        continue

    for i in range(len(strs)):
        #print(strs[:i] + strs[i+1:])
        temp = strs[:i] + strs[i+1:]
        if temp in dic :
            dic.append(strs)
            break

print (max(dic, key=len))



# import sys
# sys.stdin = open('sample.txt')
# input = sys.stdin.readline

# n, str1 = map(str, input().split())
# str_list = []


# for i in range(int(n)):
#     str_list.append(input().rstrip())       #사전에 등재된 단어만 사용가능

# dictionary = list(str1.rstrip())

# for strs in str_list :
#     for i in range(1, len(strs)-1):
#         if strs[i] not in dictionary :
#             dictionary.append(strs[i])
            
# # print(dictionary)
# temp_len = 0
# answer = ""

# for strs in str_list:                #무조건 3글자
#     # print(strs[-2:])
#     # print(strs[:2])
#     if str1[0] not in strs[:2] : #s
#         continue
#     if str1[2] not in strs[-2:] : #d
#         continue
    
#     # flag = True
#     for i in range(0, len(strs)):  #mid
#         if strs[i] not in dictionary:
#             # flag = False
#             break
#     else :
#         if str1[1] in strs[1:-1]:
#             if temp_len < len(strs) :
#                 temp_len = len(strs)
#                 answer = strs
           
# print(answer)
