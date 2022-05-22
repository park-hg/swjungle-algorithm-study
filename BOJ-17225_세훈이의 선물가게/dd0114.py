import sys

sang_time, ji_time, num = map(int, sys.stdin.readline().split())

sang_list = []
ji_list = []
time_table = [False]*86401
sang_done_time = 0
ji_done_time = 0
total_order = 0

for _ in range(num):
    order_time, RorB, order_num = map(sys.stdin.readline().split())
    order_time = int(order_time)
    order_num = int(order_num)

    if RorB == "B":
        start_time = max(order_time,sang_done_time)
        for i in range(order_num):
            done_time = start_time + i*sang_time
            mark = time_table[done_time]
            if mark == [False]:
                mark = 1
            else:
                mark =3
        sang_done_time = mark
        total_order += order_num

    else : 
        start_time = max(order_time,ji_done_time)
        for i in range(order_num):
            done_time = start_time + i*ji_time
            mark = time_table[done_time]
            if mark == [False]:
                mark = 2
            else:
                mark =3
        ji_done_time = mark
        total_order += order_num

count = 0
for i in range(86401):
    a = time_table[i]
    if a == False:
        continue
    elif a == 1 :
        count +=1
        sang_list.append(count)

    elif a == 2:
        count +=1
        ji_list.append(count)
    else :
        count +=1
        sang_list.append(count)
        count +=1
        ji_list.append(count)
    
print(len(sang_list))
for i in sang_list:
    print(i)

print(len(ji_list))
for i in ji_list:
    print(i)
