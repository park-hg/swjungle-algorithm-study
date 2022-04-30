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
    
    # print(wait_list)
    
    while left_value <= right_value :

        mid_vlaue = (left_value + right_value) // 2
        total = 0
        temp_idx = 0
        idx_list = []
        # print(mid_vlaue, end=" ")
        for i in range(M):
            
            # print(mid_vlaue % wait_list[i], end=" ")
            idx_list.append(mid_vlaue % wait_list[i])
      
            total += mid_vlaue // wait_list[i]   # 1 2 3 4 5
       
        # print("mid", mid_vlaue)
        # print("total", total)
        # print(idx_list)
        if total < N :
            left_value = mid_vlaue + 1
        else:
            right_value = mid_vlaue - 1
            answer = mid_vlaue
            for j in range(len(idx_list)):          #순서대로 가면서 
                if idx_list[j] > temp_idx:
                    temp_idx = idx_list[j]
                    answer = copy_list.index(wait_list[j]) +1

    print(answer)
            # print(idx_list)
    # print(answer)
    # print(real_idx)