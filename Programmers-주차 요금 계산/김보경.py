import math

def solution(fees, records):
    min_time, min_fee, unit_time, unit_fee = fees
    info = {}
    answer = {}
    for record in records:
        print(record)
        time, num, status = record.split(" ")
        num = int(num)
        if status == "IN" :
            info[num] = time
        else:
            in_h, in_m = map(int, info[num].split(":"))
            out_h, out_m = map(int, time.split(":"))
            time = (out_h * 60 + out_m) - (in_h * 60 + in_m)
            if num in answer:
                answer[num] += time
            else:
                answer[num] = time
            del(info[num])
        print(answer)

    if len(info) > 0 :
        for i in info.keys():
            print(i, info[i])
            in_h, in_m = map(int, info[i].split(":"))
            time = (23 * 60 + 59) - (in_h * 60 + in_m)
            if i in answer:
                answer[i] += time
            else:
                answer[i] = time
            print(answer)


    total = []
    for ans in answer.keys():
        print(ans, answer[ans])
        time = answer[ans]
        if time <= min_time :
            total.append((ans, min_fee))
        else:
            total.append((ans, min_fee + math.ceil((time - min_time) / unit_time) * unit_fee))

    total.sort()
    answer = []
    for t in total:
        num, fee = t
        answer.append(fee)
    return answer
