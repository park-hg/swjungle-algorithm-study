from math import ceil, floor

def solution(enroll, referral, seller, amount):
    answer = []
    refer_dict = {}
    result = {}

    for i in range(len(enroll)):
        refer_dict[enroll[i]] = referral[i]

    for i in range(len(seller)):
        money = amount[i] * 100
        current = seller[i]
        re = refer_dict[seller[i]]

        while re != '-' and money >= 10:
            if current in result:
                result[current] += ceil(money*0.9)
            else:
                result[current] = ceil(money*0.9)
            money = floor(money*0.1)
            current = re
            re = refer_dict[current]

        if money >= 10:
            if current in result:
                result[current] += ceil(money*0.9)
            else:
                result[current] = ceil(money*0.9)

            if refer_dict[current] in result:
                result[refer_dict[current]] += floor(money*0.1)
            else:
                result[refer_dict[current]] = floor(money*0.1)
        else:
            if current in result:
                result[current] += ceil(money*0.9)
            else:
                result[current] = ceil(money*0.9)

    for i in enroll:
        if i in result:
            answer.append(result[i])
        else:
            answer.append(0)
            
    print(answer)
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4])