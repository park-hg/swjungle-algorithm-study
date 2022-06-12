from collections import deque
import sys

def solution(gems):
    answer = [0, 1000001]
    minsize = len(set(gems))
    
    dic = {}
    q = deque()
    
    dic[gems[0]] = 1
    startIdx = 0
    endIdx = 0
        
    while True :
        
        if endIdx == len(gems) - 1 :
            
            while len(dic) >= minsize :
                
                if answer[1] - answer[0] > endIdx - startIdx :
                    
                    answer[0] = startIdx + 1
                    answer[1] = endIdx + 1
                
                if dic[gems[startIdx]] != 1:
                    dic[gems[startIdx]] -= 1
                    startIdx += 1
                else:
                    del dic[gems[startIdx]]
                    
                    if len(dic) >= minsize :
                        startIdx += 1
                    else:
                        break
                
            if answer[1] - answer[0] > endIdx - startIdx :
                answer[0] = startIdx + 1
                answer[1] = endIdx + 1
            
            break
            
        else :              
            if len(dic) < minsize :
                endIdx += 1
                
                if gems[endIdx] not in dic :
                    dic[gems[endIdx]] = 1
                else:
                    dic[gems[endIdx]] += 1
                    
                
            else :
                
                if answer[1] - answer[0] > endIdx - startIdx :
                    answer[0] = startIdx + 1
                    answer[1] = endIdx + 1
                    

                if dic[gems[startIdx]] != 1:
                    dic[gems[startIdx]] -= 1
                else:
                    del dic[gems[startIdx]]

                startIdx += 1
            
    return answer