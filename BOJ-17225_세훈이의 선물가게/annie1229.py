# 24. 세훈이의 선물가게(BOJ-17225)
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline

sangmin_packing_time, jisoo_packing_time, total_guest_count = map(int, input().split())
order_list = []
sangmin_packing_count = 0
sangmin_packing_list = []
jisoo_packing_count = 0
jisoo_packing_list = []
sangmin_last_packing_time = 0
jisoo_last_packing_time = 0

for n in range(total_guest_count):
    order_time, packing_color, gifts = input().rstrip().split()
    if packing_color == 'B': 
        sangmin_packing_count += int(gifts)
        sangmin_last_packing_time = max(int(order_time), sangmin_last_packing_time)
        for c in range(int(gifts)):
            packing = (sangmin_last_packing_time + (c * sangmin_packing_time), packing_color)
            heappush(order_list, packing)
        sangmin_last_packing_time += (int(gifts) * sangmin_packing_time)
    else: 
        jisoo_packing_count += int(gifts)
        jisoo_last_packing_time = max(int(order_time), jisoo_last_packing_time)
        for c in range(int(gifts)):
            packing = (jisoo_last_packing_time + (c * jisoo_packing_time), packing_color)
            heappush(order_list, packing)
        jisoo_last_packing_time += (int(gifts) * jisoo_packing_time)

gift_idx = 1
while order_list:
    packing_time, packing_color = heappop(order_list)
    print(packing_time, packing_color)
    if packing_color == 'B':
        sangmin_packing_list.append(str(gift_idx))
    else:
        jisoo_packing_list.append(str(gift_idx))
    gift_idx += 1

print(sangmin_packing_count)
print(' '.join(sangmin_packing_list))
print(jisoo_packing_count)
print(' '.join(jisoo_packing_list))

