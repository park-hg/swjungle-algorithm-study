#re
def solution(info, query):
    answer = []
    
    for qinfo in query :
        query_list = list(map(str, qinfo.split(" and ")))
        food, score = query_list[-1].split(" ")
        del query_list[-1]
        query_list.append(food)
        query_list.append(score)
        # print(query_list)
        cnt = 0
        for col in info : 
            info_list = list(map(str, col.split(" ")))
          
            for i in range(len(query_list)-1):
                if query_list[i] == '-' :
                    continue                
                if query_list[i] != info_list[i] :
                    break
            else :
                if int(query_list[-1]) <= int(info_list[-1]) :
                    cnt += 1
        answer.append(cnt)
        
    return answer