#실패
import sys
import copy
sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
wait_list = list(map(int, input().split()))
answer = 0
if N <= len(wait_list) :
    # print(wait_list[N-1])
    # answer = wait_list.index(wait_list[N-1])+1   # 1~
    # print(answer)
    print(N)

else:
    copy_list = copy.deepcopy(wait_list)
    wait_list.sort()
    # print(wait_list)
    left_value = 0
    right_value = wait_list[-1] * N
    answer = 0
    total_people = N #N-M
    # print(wait_list)
    
    while left_value <= right_value :

        mid_vlaue = (left_value + right_value) // 2
        total = 0
        temp_value = wait_list[-1]
        temp_idx = 0
        idx_list = []
        # onemin_list = []

        # print(mid_vlaue, end=" ")
        for i in range(M):
            
            # print(mid_vlaue % wait_list[i], end=" ")
            idx_list.append(mid_vlaue % wait_list[i])
            # onemin_list.append((mid_vlaue-1) % wait_list[i])
            
            total += mid_vlaue // wait_list[i]   # 1 2 3 4 5
       
        print("mid", mid_vlaue)
        # print("total", total)
        print(idx_list)

        if total < total_people :
            left_value = mid_vlaue + 1
        else:
            right_value = mid_vlaue - 1
            
            for j in range(len(idx_list)):          #순서대로 가면서 
                if idx_list[j] <= temp_value:
                    temp_value = idx_list[j]
                    temp_idx = j
                    answer = copy_list.index(wait_list[temp_idx])+1 

    print(answer)
 
