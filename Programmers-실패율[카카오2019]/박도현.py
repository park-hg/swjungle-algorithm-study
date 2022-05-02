def solution(N, stages):
    answer = []
    clear = [0]*(N+2)
    dodal = [0]*(N+2)
    ans = []
    ans2 = []
    for i in stages:
        for j in range(1,i+1):
            dodal[j] +=1
            clear[j] +=1
        clear[i] -= 1
    
    for i in range(1,N+1):
        if dodal[i] != 0:
            a = clear[i]/dodal[i]
            ans.append(a)
            ans2.append(a)
        else :
            ans.append(0)
            ans2.append(0)
    
    ans2.sort()
    
    for i in range(len(ans)):
        a = ans.index(ans2[i])
        answer.append(a+1)
        ans[a] = 2
    
    return answer

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
# print(solution(4, [1, 2, 2, 2, 0]))
# print(solution(3, [1, 1, 1]))