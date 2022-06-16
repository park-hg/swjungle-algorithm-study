from itertools import permutations

def solution(expression):
    answer = 0
    for op1, op2 in permutations(["+", "-", "*"], 2):
        l = expression.split(op1)
        temp = []
        for ll in l:
            lll = list(map(eval, ll.split(op2)))
            lll = [str(i) for i in lll]
            temp.append(eval(op2.join(lll)))
        temp = [str(i) for i in temp]
        answer = max(answer, abs(eval(op1.join(temp))))
    return answer