s = input()

s_len = len(s)
num = 0

if s_len <= 9:
    num = s_len
else :
    num = 9+(s_len-9)//2

first = ([],s,num)
q = [first]
answer =[]

while q:
    pop = q.pop()
    n_list = pop[0]
    r_list = pop[1]
    r_num = pop[2]
    
    for i in range(1,3):
        new_num = pop[1][0:i]
        new_list = pop[1][i:]
        remain = r_num -1

        if new_num in n_list:
            continue
        
        else:
            if r_num == 0 and r_list == "":
                print(new_num)
                break
            else :
                n_list.append(new_num)
                q.append((n_list,r_list,r_num))