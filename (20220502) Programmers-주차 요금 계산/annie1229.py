from math import ceil

def solution(fees, records):
    def time_to_minute(time):
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute
    
    flag_dict = {}
    records_dict = {}
    total_time = {}
    total_cost = []

    for record in records:
        time, car_number, case = record.split()
        if case == 'IN':
            records_dict[car_number] = time_to_minute(time)
            flag_dict[car_number] = True
        else:
            acc_time = time_to_minute(time) - records_dict[car_number]
            records_dict[car_number] = 0
            flag_dict[car_number] = False
            if car_number in total_time:
                total_time[car_number] += acc_time
            else:
                total_time[car_number] = acc_time

    for car_number, time in records_dict.items():
        if flag_dict[car_number]:
            acc_time = time_to_minute("23:59") - time
            # print(car_number, "23:59에 출차!", acc_time)
            records_dict[car_number] = 0
            if car_number in total_time:
                total_time[car_number] += acc_time
            else:
                total_time[car_number] = acc_time

    for car_number, acc_time in total_time.items():
        if acc_time > fees[0]:
            total_cost.append((car_number, (fees[1] + ceil((acc_time - fees[0]) / fees[2]) * fees[3])))
        else:
            total_cost.append((car_number, fees[1]))
    # print(records_dict)
    # print(total_time)
    total_cost.sort()
    # print(total_cost)
    result = []
    for cost in total_cost:
        result.append(cost[1])
    print(result)
    return result

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])