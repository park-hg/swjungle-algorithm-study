
def solution(n, k):
    q = n
    r = ""
    a_list =[]
    max_a = 0
    answer = 0
    check = []
    
    while q != 0:
        q,ptr = q // k, q%k

        if ptr == 0 and r != "":
            a_list.append(int(r))
            max_a = max(max_a, int(r))
            r = ""
            
        elif ptr != 0 :        
            r = str(ptr)+r
    
    a_list.append(int(r))
    max_a = max(max_a, int(r))  

    if max_a < 5:
        check = [False]*5
        check[2] = True
        check[3] = True
    
    else : 
    # max_a >= 5
        check = [False]*(max_a+1)
        check[2] = True
        check[3] = True
        for i in range(5,max_a+1,2):
            for j in range(3,i,2):
                if j**2 > i:
                    check[i] = True
                    break
                elif check[j] == True :
                    if i%j == 0:
                        break
                    
    for i in a_list:
        if check[i] == True:
            answer += 1

    return answer

nn = 6
kk = 3

print(solution(nn,kk))