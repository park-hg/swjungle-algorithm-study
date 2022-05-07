from collections import deque

def solution(enroll, referral, seller, amount):
    
    n = len(enroll)
    ind = [0] * n
    answer = [0] * n
    q = deque([])
    branch = [False]*n
    money = [0]*n

    for i in range(n):
        if referral[i] != "-":
            ptr = enroll.index(referral[i])
            ind[ptr] += 1
            branch[i] = ptr

    for i in range(len(seller)):
        na = seller[i]
        money[enroll.index(na)] = amount[i] *100

    for i in range(n):
        if ind[i] == 0:
            q.append(i)

    while q:
        num = q.popleft()
        
        earn = money[num] +answer[num]           
        # 번돈 저장. 0.9
        answer[num] = earn - (earn//10)

        br_num = branch[num] 
        # 브랜치 있으면 상납금 전달
        if br_num:
            answer[br_num] += earn//10
            ind[br_num] -= 1
            if ind[br_num] == 0 :
                q.append(br_num)

    return answer

en = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
ref = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
sel = ["young", "john", "tod", "emily", "mary"]
amo = [12, 4, 2, 5, 10]
solution(en, ref, sel, amo)

en = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
ref = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
sel = ["sam", "emily", "jaimie", "edward"]
amo = [2, 3, 5, 4]

solution(en, ref, sel, amo)