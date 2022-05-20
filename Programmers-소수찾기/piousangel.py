def chkSosu(arr):
    global answer
    global temp_list
    temp = ''
    for i in range(len(arr)):
        temp += arr[i]
    temp_int = int(temp)
    if temp_int not in temp_list:
        temp_list.append(temp_int)
    
    return 

def dfs(n_list, box, visited, idx, lenOfNum):
    
    if idx == lenOfNum:
        chkSosu(box)
        return
        
    for i in range(0, len(n_list)):
        if visited[i] != True:
            visited[i] = True
            box[idx] = n_list[i]
            dfs(n_list, box, visited, idx+1, lenOfNum)
            visited[i] = False

answer = 0
temp_list = []
def solution(numbers):
    global answer
    global temp_list
    n_list = []
    
    for i in numbers:
        n_list.append(i)
    
    visited = [False] * len(n_list)
    
    for i in range(1, len(n_list)+1):
        box = [0] * i
        dfs(n_list, box, visited, 0, i)
    
    # print(temp_list)
    for k in temp_list:
        if k == 0 or k == 1:
            continue

        for i in range(2, k):
            if k % i == 0:
                break
        else:   
            answer += 1
        
    return answer