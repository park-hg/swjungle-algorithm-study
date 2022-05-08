# 30 + 14 = 44
def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    ptr = k
    delete = []
    
    if 'C' not in cmd:
        return "".join(answer)
        
    for command in cmd:
        c = command[0]
        if c == 'U':
            move = command.split()[1]
            ptr -= int(move)
        elif c == 'D':
            move = command.split()[1]
            ptr += int(move)
        elif c == 'C':
            delete.append(ptr)
            answer.pop()
            ptr = min(ptr, len(answer) - 1)
        else: # c == 'Z'
            del_last = delete.pop()
            answer.append('O')
            if del_last <= ptr:
                ptr += 1
    
    while delete:
        pop = delete.pop()
        answer = answer[:pop] + ['X'] + answer[pop:]

    return "".join(answer)