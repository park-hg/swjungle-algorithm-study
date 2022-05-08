ptr = 0
klist = []
q = []
length = 0

def find_up(p):

def find_down(p):

def sol(a):
    global length
    global ptr
    if a[0] == "D":
        ptr += a[2]
        while klist[ptr] == 1:
            ptr +=1

    elif a[0] == "U":
        ptr -= a[2]
        while klist[ptr] == 1:
            ptr -=1

    elif a[0] == "C":
        klist[ptr] = 0
        ptr += 1


    else :

        
def solution(n, k, cmd):
    global ptr
    global length
    
    length = n
    klist =[1]*n    
    ptr = k



    answer = ''
    return answer



solution (8, 2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])

solution (8, 2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])