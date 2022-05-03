import math

def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def solution(fees, records):
    d = {}
    for record in records:
        time, car_num, is_in = record.split()
        time = time_to_minute(time)
        if car_num not in d:
            d[car_num] = (-time, True)
        else:
            cur_time = d[car_num][0]
            if is_in == 'IN':
                d[car_num] = (cur_time - time, True)
            else:
                d[car_num] = (cur_time + time, False)
    
    for car_num in d:
        if d[car_num][1]:
            cur_time = d[car_num][0]
            d[car_num] = (cur_time + 23*60+59, False)

    d_fee = {}
    for car_num in d:
        time = d[car_num][0]
        fee = fees[1] + math.ceil(max(0, (time - fees[0]))/fees[2])*fees[3]
        d_fee[int(car_num)] = fee

    answer = [fee for _, fee in sorted(d_fee.items())]
    return answer