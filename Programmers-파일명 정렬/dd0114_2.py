def solution(files):
    answer = []
    s_list =[]
    num_list = ["1","2","3","4","5","6","7","8","9","0"]
    for file in files:
        head = ""
        number = ""
        tail = ""
        lam = ""
        low_w = ""
        for i in range(len(file)):
            if file[i] in num_list:
                break
        head = file[:i]
        file = file[i:]        
        for i in head:
            low_w = low_w + i.lower()

        for i in range(len(file)):
            if file[i] not in num_list:
                break

        if i > 5 :
            i = 5
        elif file[i] in num_list:
            i +=1

        number = file[:i]

        if i+1 < len(file):
            tail = file[i:]

        # tmp = 5 - len(number)
        # lam = "0"*tmp + number
        lam = int(number)

        s_list.append((head,number,tail,lam,low_w))

    s_list.sort(key = lambda x : (x[3]))
    s_list.sort(key = lambda x : (x[4]))

    for i in s_list:
        word = i[0]+i[1]+i[2]
        answer.append(word)
    
    return answer

# files =["O00321", "O49qcGPHuRLR5FEfoO00321"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))