from re import A


a = "AE"

def solution(word):
    mul_l = [781,156,31,6,1]
    answer = 0
    for i in range(len(word)):
        if word[i] == 'A':
            answer += 1
        elif word[i] == "E":
            answer += mul_l[i]*1+1
        elif word[i] == "I":
            answer += mul_l[i]*2+1
        elif word[i] == "O":
            answer += mul_l[i]*3+1
        elif word[i] == "U":
            answer += mul_l[i]*4+1
    
    return answer
print(solution(a))