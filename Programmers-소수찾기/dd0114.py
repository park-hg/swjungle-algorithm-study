from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    
    numbers.sort(reverse=True)
    max_num = ""

    for i in numbers:
        max_num += i

    max_num = int(max_num)

    sosu_list = [False] * (max_num+1)
    sosu_list[2] = True
    sosu_list[3] = True

    if max_num <= 1:
        return 0
    if max_num <= 3:
        return 1
    if max_num == 4:
        return 0

    for i in range(5,max_num+1,2):
        for j in range(3,i,2):
            if sosu_list[j] == True:
                if i % j == 0:
                    break
                elif j**2 > i :
                    sosu_list[i] = True
    
    ans_list = set([])

    for i in range(1,len(numbers)):
        a = list(permutations(numbers,i))
        for j in a:
            add_num =''
            for h in j:
                add_num+=h
            ans_list.add(add_num)

    answer = 0
    for i in add_num:
        if sosu_list[int(i)] == True:
            answer +=1

    return answer


numbers = "17"
print(solution(numbers))
