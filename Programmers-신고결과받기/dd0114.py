import sys

def solution(id_list, report, k):
    leng = len(id_list)
    push = [1<<leng-10]*leng
    pull = [0]*leng
    
    for i in range(report):
        sh, ll = map(int,sys.stdin.readline().rstrip())
        

    answer = []
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
k = 2	
# [2,1,1,0]
# id_list = ["con", "ryan"]	
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]	
# k = 3	
# # [0,0]