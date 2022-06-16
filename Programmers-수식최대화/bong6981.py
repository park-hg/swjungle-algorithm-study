from collections import defaultdict
from itertools import permutations

def solution(expression):
    exp = list(expression)
    
    info = defaultdict(list)
    
    ops = ['+', '-', '*']
    used_ops = set()
    start = 0
    idx = 0
    new_exp = []

    while idx < len(exp):
        if exp[idx] in ops:
            new_exp.append(''.join(exp[start:idx]))
            start = idx + 1
            used_ops.add(exp[idx])
            info[exp[idx]].append(len(new_exp))
            new_exp.append(exp[idx])
        if idx == len(exp) -1 :
            new_exp.append((''.join(exp[start:idx+1])))

        idx += 1
    exp = new_exp
    print(new_exp)
    print(info)
    ans = 0
    ## 가능한 우선순위 순서  
    for p in permutations(list(used_ops)):
        order = list(p)
        tmp_exp = exp[::]
        print("====", order)
        for op in order:
            for idx in info[op]:
                ##find_prev
                prev = idx -1 
                prev_num =0
                while(prev >= 0):
                    if tmp_exp[prev] == '#':
                        prev -= 1
                    else:
                        prev_num = int(tmp_exp[prev])
                        break
                ##find_next
                next_ = idx + 1 
                next_num = 0
                while next_ < len(exp):
                    if tmp_exp[next_] == '#':
                        next_ += 1
                    else:
                        next_num = int(tmp_exp[next_])
                        break
                num = 0
                if op == '+':
                    num = prev_num + next_num
                elif op == '-':
                    num = prev_num - next_num
                elif op == '*':
                    num = prev_num * next_num

                for i in range(prev, next_ + 1):
                    tmp_exp[i] = '#'
                tmp_exp[idx] = str(num)
                print(tmp_exp)
        for e in tmp_exp:
            if e != "#":
                print(int(e))
                ans = max(ans, abs(int(e)))
        
    return ans


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))


