# 신고 횟수 제한 없음 다른유저는 계속 신고가능
# 한유저 여러번 신고가능 동일유저에 대한 신고는 1회로
# k번 이상 신고유저 게시판 이용 정지
# 해당 유저를 신고한 모든 유저에게 정지메일
# 한번에 정지시키면서 정지 메일 

from collections import defaultdict
from collections import deque

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    mapping = defaultdict()
    idx = 0
    graph = [[] for _ in range(len(id_list))]
    for name in id_list :
        mapping[name] = idx
        idx +=1
    
    dic = {}
    temp_list = []
    for info in report :
        a, b = map(str, info.split(" "))
        if mapping[b] not in graph[mapping[a]] : #중복 제거 
            graph[mapping[a]].append(mapping[b])
            if mapping[b] not in dic :
                dic[mapping[b]] = 1
            else:
                dic[mapping[b]] += 1
                if dic[mapping[b]] >= k and mapping[b] not in temp_list :
                    temp_list.append(mapping[b])
    
   
    
    for i in range(len(graph)):
        if len(graph[i]) == 0 :
            continue
        for j in graph[i] :
            if j in temp_list :
                answer[i] += 1

    return answer