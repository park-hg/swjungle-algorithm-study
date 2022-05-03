
import math

def solution(fees, records):
    check = {}

    for record in records:
        time, number, status = record.split()
        time = time.split(':')
        time = int(time[0])*60 + int(time[1])
        if number not in check:
            check[number] = (0, time, status)
        if status == 'IN':
            check[number] = (check[number][0], time, status)
        elif status == 'OUT':
            total_time, in_time, _ = check[number]
            total_time += time - in_time
            check[number] = (total_time, time, status)

    result = {}

    for number in check.keys():
        total_time, time, status = check[number]
        if status == 'IN':
            total_time += 1439 - time
        fee = fees[1]
        if total_time <= fees[0]:
            result[number] = fee
        else:
            fee = fee + math.ceil((total_time - fees[0]) / fees[2]) * fees[-1]
            result[number] = fee

    return list(map(lambda x : x[1], sorted(result.items())))


