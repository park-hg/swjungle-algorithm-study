from collections import deque     
import copy

#죄송합니다 안풀리네요


def chkWire(wires, idx):
    cnt = 0
    w_list = copy.deepcopy(wires)

    q = deque()
    q.append(w_list[idx][1])
    del w_list[idx]
  
    while q:
        
        k = q.popleft()
        
        for i in range(len(w_list)):

            flag = False
            temp = w_list[i]

            if temp[0] == k :
                q.append(temp[1])
                # del w_list[i]
                w_list.remove(temp)
                flag = True
                
            elif temp[1] == k :
                q.append(temp[0])
                # del w_list[i]
                w_list.remove(temp)
                flag = True
                              
            if flag:
                i -= 1
        
        cnt +=1
        
    return cnt

def solution(n, wires):
    minValue = 10001

    for i in range(len(wires)) :
        leftWire = chkWire(wires, i)
        rightWire = n - leftWire
        temp = abs(leftWire - rightWire)
        minValue = min(minValue, temp)
        
    return minValue