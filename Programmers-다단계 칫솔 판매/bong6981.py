def solution(enroll, referral, seller, amount):
    idx = {}
    for i, p in enumerate(enroll):
        idx[p] = i
    idx["-"] = len(enroll)

    answer = [0] * (len(enroll)+1)    
    for i, s in enumerate(seller):
        sub = s
        money = amount[i] * 100
        while True:
            if sub == "-":
                break
            if int(money * 0.1) < 1:
                answer[idx[sub]] += money
                break
            to_give = int(money * 0.1) 
            answer[idx[sub]] += (money - to_give)
            money = to_give
            sub = referral[idx[sub]]
        
    return answer[:-1]


