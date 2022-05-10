ptr = 0
klist = []
q = []
length = 0

def sol(a):
    global length
    global ptr
    global klist

    if a[0] == "D":
        ptr += int(a[2])
        while klist[ptr] == 0:
            ptr +=1

    elif a[0] == "U":
        ptr -= int(a[2])
        while klist[ptr] == 0:
            ptr -=1

    elif a[0] == "C":
        klist[ptr] = 0
        q.append(ptr)
        save_p = ptr
        ptr += 1
        
        if ptr == length:
            ptr -=1
            while klist[ptr] == 0:
                ptr -=1
                if ptr == -1:
                    break
        else :
            while klist[ptr] == 0:
                ptr +=1
                if ptr == length:
                    ptr = save_p
                    break

            if ptr == save_p:
                while klist[ptr] == 0:
                    ptr -=1
                    if ptr == -1:
                        break
    else :
        rb = q.pop()
        klist[rb] = 1

def solution(n, k, cmd):
    global ptr
    global length
    global klist

    length = n
    klist =[1]*n    
    ptr = k

    for i in cmd :
        sol(i)

    answer = ''    
    for i in range(length) :
        if i ==1:
            answer += klist[i]

    return answer



solution (8, 2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])

solution (8, 2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])