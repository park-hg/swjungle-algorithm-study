import copy 

def solution(expression):
    ex_list = []
    buf = ""
    smm = ["+","-","*"]
    for i in expression:
        if i not in smm:
            buf += i
        else :
            ex_list.append(int(buf))
            ex_list.append(i)
            buf = ""

    ex_list.append(int(buf))

    a = [(0,1,2),(0,2,1),(1,2,0),(1,0,2),(2,1,0),(2,0,1)]

    answer = 0

    for i in a:
        new_list = copy.deepcopy(ex_list)
        for j in i:
            tmp = smm[j]
            while tmp in new_list:
                ind = new_list.index(tmp)
                
                if tmp == "+":
                    new = new_list[ind-1] + new_list[ind+1]

                elif tmp == "-":
                    new = new_list[ind-1] - new_list[ind+1]

                else :
                    new = new_list[ind-1] * new_list[ind+1]

                new_list = new_list[:ind-1]+[new]+new_list[ind+2:]
        
        answer = max(answer, abs(new_list[0]))

    return answer


a = "100-200*300-500+20"
b = "50*6-3*2"

print(solution(a))
print(solution(b))