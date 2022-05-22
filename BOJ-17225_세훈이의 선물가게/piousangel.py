import sys
from collections import deque
import heapq
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 파란색(B) 상민, 빨간색(R) 지수
# 상민 몇개, 선물 번호  / 지숫 몇개, 선물 번호

total_t = 0  #계속 돌면서 확인 해줘야 해요
sangmin_list = []
jisu_list = []
info_list = []
blue_t, red_t, n = map(int, input().split())


all_info_list = []
#예제 2에서
# s_t = 2 = B
# j_t = 3 = R

for i in range(n):
    #list(map(str, input().split())에는 주문시각, 포장지 색, 선물 갯수
    info_list.append(list(map(str, input().split())))

for info in info_list :
    # temp_time = 0
    temp_time = int(info[0])
    for i in range(int(info[2])):    
        if info[1] == 'R' :
            heapq.heappush(all_info_list, [temp_time, 'R']) #[temp_time, temp_time + red_t]
            # all_info_list.append([temp_time, temp_time + red_t])
            temp_time += red_t
        else :
            heapq.heappush(all_info_list, [temp_time, 'B']) #[temp_time, temp_time + blue_t]
            # all_info_list.append([temp_time, temp_time + blue_t])
            temp_time += blue_t

gift_idx = 1
while len(all_info_list) > 0 :
    if heapq.heappop(all_info_list)[1] == 'R' :
        jisu_list.append(gift_idx)
        gift_idx += 1
    else:
        sangmin_list.append(gift_idx)
        gift_idx += 1

print(len(sangmin_list))
for i in sangmin_list :
    print(i, end = " ")
print()
print(len(jisu_list))
for i in jisu_list :
    print(i, end = " ")
