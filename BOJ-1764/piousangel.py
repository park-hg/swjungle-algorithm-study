import sys
input = sys.stdin.readline

dic = {}
a, b = map(int, input().split())

for i in range(a+b) :
    name = input().rstrip()
    if name not in dic :
        dic[name] = 1
    else:
        dic[name] += 1

sorted_dic = sorted(dic.items())
cnt = 0
answer_list = []
for info in sorted_dic :
    if info[1] == 2 :
        cnt += 1
        answer_list.append(info[0])

print(cnt)
for i in answer_list :
    print(i)