from collections import defaultdict


def calc(a, b, mod):
    temp = (a - b) / mod

    if temp <= 0:
        return 0

    if 0 < temp - ((a - b) // mod):
        return int(temp) + 1

    return int(temp)


def solution(fees, records):

    carlist = defaultdict(list)  # carlist => 총 시간
    car_time = defaultdict(list)  # car_time => 입차 하고 남아있는 시간 저장

    for data in records:
        time, car_num, io = map(str, data.split())
        hour, min = map(int, time.split(':'))
        time_val = hour * 60 + min
        if io == 'IN':
            car_time[car_num] = time_val
        else:
            if carlist[car_num]:
                carlist[car_num] += time_val - car_time[car_num]
            else:
                carlist[car_num] = time_val - car_time[car_num]
            car_time[car_num] = -1

    for ct in car_time:
        if car_time[ct] != -1:
            if carlist[ct]:
                carlist[ct] += 1439 - car_time[ct]
            else:
                carlist[ct] = 1439 - car_time[ct]

    result = []
    for fee in list(sorted(carlist.items(), key=lambda x: x[0])):
        result.append(fees[1] + (calc(fee[1], fees[0], fees[2]) * fees[3]))

    return result
