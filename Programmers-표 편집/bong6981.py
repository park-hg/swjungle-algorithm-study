## 28 + 63 = 91 
def solution(n, k, cmd):

    data = []
    data.append([-1, 1, True])
    for i in range(1, n-1):
        data.append([i-1, i+1, True])
    data.append([n-2, -1, True])

    print(data)

    selected = k
    recent_deleted = []

    for c in cmd:
        c = c.split()
        print(c, selected)
        if c[0] == 'U':
            for _ in range(int(c[1])):
                selected = data[selected][0]
                while not data[selected] :
                    selected = data[selected][0]
            print(selected)
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                selected = data[selected][1]
                while not data[selected]:
                    selected = data[selected][1]
            print(selected)
        elif c[0] == 'C':
            recent_deleted.append(selected)
            prev = data[selected][0]
            next = data[selected][1]

            if next != -1:
                data[next][0] = prev
            if prev != -1:
                data[prev][1] = next
            
            data[selected][2] = False
            if selected == (n-1):
                selected = data[selected][0]
            else:
                selected = data[selected][1]
        else:
            rd = recent_deleted.pop()
            prev = data[rd][0]
            next = data[rd][1]

            if next != -1:
                data[next][0] = rd
            if prev != -1:
                data[prev][1] = rd
            data[rd][2] = True
        print(c, data)
    
    answer = ''
    for d in data:
        if d[2] :
            answer += 'O'
        else:
            answer += 'X'

    return answer

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] ))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
