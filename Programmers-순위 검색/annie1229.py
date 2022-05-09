# 시간초과...해결중..
def solution(info, query):
    answer = []
    people = []
    
    for i in info:
        lang, fb, js, pc, score = i.strip().split()
        data = 0
        if lang == 'cpp':
            data = (1 << 0)
        elif lang == 'java':
            data = (1 << 1)
        elif lang == 'python':
            data = (1 << 2)
        if fb == 'backend':
            data |= (1 << 3)
        elif fb == 'frontend':
            data |= (1 << 4)
        if js == 'junior':
            data |= (1 << 5)
        elif js == 'senior':
            data |= (1 << 6)
        if pc == 'chicken':
            data |= (1 << 7)
        elif pc == 'pizza':
            data |= (1 << 8)
        people.append((int(score), data))

    people.sort()

    count = 0
    for q in query:
        count = 0
        arr = q.split(' and ')
        arr[-1], score = arr[-1].strip().split()
        lang, fb, js, pc = arr

        pass_info = 0
        if lang == '-':
            pass_info = 0
        elif lang == 'cpp':
            pass_info = (1 << 0)
        elif lang == 'java':
            pass_info = (1 << 1)
        elif lang == 'python':
            pass_info = (1 << 2)
        if fb == '-':
            pass_info &= ~((1 << 3) | (1 << 4))
        elif fb == 'backend':
            pass_info |= (1 << 3)
        elif fb == 'frontend':
            pass_info |= (1 << 4)
        if js == '-':
            pass_info &= ~((1 << 5) | (1 << 6))
        elif js == 'junior':
            pass_info |= (1 << 5)
        elif js == 'senior':
            pass_info |= (1 << 6)
        if pc == '-':
            pass_info &= ~((1 << 7) | (1 << 8))
        elif pc == 'chicken':
            pass_info |= (1 << 7)
        elif pc == 'pizza':
            pass_info |= (1 << 8)
            
        for p in people:
            if p[0] >= int(score) and p[1] & pass_info == pass_info:
                count += 1
        answer.append(count)       
    return answer
