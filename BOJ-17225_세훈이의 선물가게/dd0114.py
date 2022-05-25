import sys

sang_time, ji_time, num = map(int, sys.stdin.readline().split())

sang_list = []
ji_list = []
time_table = [False]*87000
sang_done_time = 0
ji_done_time = 0
total_order = 0

for _ in range(num):
    order_time, RorB, order_num = map(str,sys.stdin.readline().split())
    order_time = int(order_time)
    order_num = int(order_num)

    if RorB == "B":
        start_time = max(order_time,sang_done_time)
        for i in range(order_num):
            done_time = start_time + i*sang_time
            
            if time_table[done_time] == False:
                time_table[done_time] = (1,0)
            else:
                time_table[done_time] = (time_table[done_time][0]+1,time_table[done_time][1])

        sang_done_time = done_time
        total_order += order_num

    else : 
        start_time = max(order_time,ji_done_time)
        for i in range(order_num):
            done_time = start_time + i*ji_time
            mark = time_table[done_time]
            if time_table[done_time] == False:
                time_table[done_time] = (0,1)
            else:
                time_table[done_time] = (mark[0],mark[1]+1)

        ji_done_time = done_time
        total_order += order_num

count = 0
for i in range(86401):
    a = time_table[i]
    if a == False:
        continue
    else :
        for _ in range(a[0]):
            count += 1
            sang_list.append(count)

        for _ in range(a[1]):
            count += 1
            ji_list.append(count)

    if count == total_order:
        break

print(len(sang_list))
print(*sang_list, sep=' ')

print(len(ji_list))
print(*ji_list, sep=' ')
