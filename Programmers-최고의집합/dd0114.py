def solution(n, s):
    answer = []
    mok = s // n
    nam = s % n
    
    if mok == 0:
        return [-1]

    for i in range(n-nam):
        answer.append(mok)
            
    for i in range(nam):
        answer.append(mok+1)

    
    return answer