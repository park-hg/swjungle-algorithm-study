s = input()
s_len = len(s)

if s_len <= 9:
    for i in s:
        print(i,end=' ')

else :
    num = 9+(s_len-9)//2
    check_default = (1<<(num+1))-1
    first = ("",s,check_default)
    q = [first]

    while q:
        pop = q.pop()

        for i in range(1,3):
            n_list = pop[0]
            r_list = pop[1]
            check = pop[2]
        
            new_num = r_list[0:i]
            r_list = r_list[i:]
            
            if 1<<int(new_num) & check == 1<<int(new_num):
                n_list += new_num+" "
                check = check - (1<<int(new_num))

                if check == 1 and r_list == "":
                    print(n_list)
                    exit(0)
                else :
                    q.append((n_list,r_list,check))