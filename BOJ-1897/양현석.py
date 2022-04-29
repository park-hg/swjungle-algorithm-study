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
        print(strs[:i] + strs[i+1:])
        temp = strs[:i+1] + strs[i+2:]
        if temp in dic :
            dic.append(strs)
            break

print (max(dic, key=len))






    