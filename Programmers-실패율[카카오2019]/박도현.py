def solution(N, stages):
    answer = []
    clear = [0]*len(stages+1)
    dodal = [0]*len(stages+1)
    ans = []
    ans2 = []
    for i in stages:
        for j in range(1,len(i)):
            dodal[j] +=1
            clear[j] +=1
        clear[i] -= 1
    
    for i in range(1,N+1):
        a = clear[i]/dodal[i]
        ans.append(a)
        ans2.append(a)
    
    ans2.sort()
    
    for i in range(1,len(ans)):
        a = ans2.index(ans[i])
        answer.append(a)
        ans2[a] = 2
    
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(4, [1, 2, 2, 2, 0]))
print(solution(3, [1, 1, 1]))