import sys
input = sys.stdin.readline

pa_n, dak_n = map(int, input().split())
pa_list = []
for i in range(pa_n) :
    pa_list.append(int(input()))

pa_list.sort()
left = 1
right = pa_list[-1]
mid = 0
temp = 0
answer = 0
# print(pa_list)

while left <= right :
    
    mid = (right + left) // 2
      
    total = 0
    for pa in pa_list :
        total += pa // mid
    
    # print("mid", mid)
    # print("total", total)
    if total >= dak_n :
        temp = mid
        left = mid +1
    else:
        right = mid -1

answer = sum(pa_list) - (temp * dak_n)

# for pa in pa_list :""
#     answer += pa % temp

print(answer)


