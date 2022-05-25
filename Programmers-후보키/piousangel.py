# 유일성  릴레이션에 있는 모든 튜플에 대해 유일하게 식별
# 최소성 : 최소한의 숫자로 유일성을 만족해야 함
# 예제에서 학번 / 나이, 전공 / 이름학년, 이름전공, 전공학년 -> 이 3개부터는 해당 안됌

def solution(relation):
    
    dic = {}
    for i in range(len(relation[0])):
        dic[i] = []  #4개 만들고
        
    for i in range(len(relation)):
        for j in range(len(relation[0])):       
            dic[j].append(relation[i][j])
   

    #이런식으로 제거할거임
    # for i in range(len(dic)):
    #     if len(set(dic[i])) == len(dic[i]):  #하나의 키로 구분 가능한 것
    #         temp += 1
    #         del dic[i]

answer
def chk_answer(arr, dic) :
    global answer
    temp_list = []
    
    for i in range(len(relation)):
        temp_str = ""
        for j in range(len(arr)) :
            temp_str += dic[i]
        temp_list.append(temp_str)
        
    for i in range(len(temp_list)):
        if len(set(temp_list[i])) == len(temp_list[i]):  #하나의 키로 구분 가능한 것
        
    answer += 1
        
        
def dfs(dic, visited, arr, idx, max_idx) :
    
    if idx == max_idx :
        chk_answer(arr, dic)
    
    for i in range(max_idx) :
        if visited[i] != True :
            visited[i] = True
            arr[idx] = dic[i]
            dfs(dic, visited, arr, idx+1, max_idx)
            visited[i] = False
    
    
    for i in range(1, len(relation)):
        visited = [False] * len(relation)
        arr = [0] * len(relation)
        
        dfs(dic, visited, arr, 0, i)
    
    print(dic)
    return answer