import copy
import sys
sys.setrecursionlimit(10000)

cnt = 0
answer = []
def jool(n_list,check,num,k):
    global cnt
    global answer

    for i in range(1,num+1):
        if cnt == k:
            return

        if (check & 1<<i) == (1<<i):
            new_check = check - (1<<i)
            new_list = copy.deepcopy(n_list)
            new_list.append(i)
            
            if new_check == 1<<0:
                cnt += 1
                if cnt == k:
                    answer = copy.deepcopy(new_list)
            else:
                jool(new_list,new_check,num,k)
                

def solution(n, k):
    global cnt
    global answer

    start_check = (1<<(n+1))-1
    start_list = []

    jool(start_list,start_check,n,k)

    return answer

nn = 5
kk = 3

print(solution(nn,kk))