def solution(files):
    temp = []
    for i, file in enumerate(files):
        head = ""
        number = ""
        flag = True
        for s in file:
            if not s.isdigit():
                if flag:
                    head += s.lower()
                else:
                    break
            else:
                flag = False
                number += s
        temp.append([head, int(number), i])
    temp.sort()
    answer = [files[i] for _, _, i in temp]
    
    return answer