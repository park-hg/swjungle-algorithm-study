from math import ceil

def solution(fees, records):
    def time_to_minute(time): # hh:mm을 분으로 변환하는 함수
        hour, minute = map(int, time.split(':'))
        return hour * 60 + minute
    
    flag_dict = {} # 출차 여부 확인하기 위한 딕셔너리
    records_dict = {} # 이전 입차시간(분) 저장하기 위한 딕셔너리
    total_time = {} # 누적 주차시간 저장하기 위한 딕셔너리
    total_cost = [] # 총 누적 주차비용 담기위한 배열

    for record in records:
        time, car_number, case = record.split()
        if case == 'IN':
            records_dict[car_number] = time_to_minute(time) # 입차시간 분으로 변환한거 저장하기
            flag_dict[car_number] = True # 입차했으면 차량 번호 flag True로
        else:
            acc_time = time_to_minute(time) - records_dict[car_number] # 출차시간(분)에서 입차시간(분) 뺀 시간
            records_dict[car_number] = 0 # 이전 입차시간 초기화
            flag_dict[car_number] = False # 출차했으면 차량 번호 flag False로
            if car_number in total_time: # 이전에 누적 주차시간이 있으면
                total_time[car_number] += acc_time # 누적 주차시간 더해주기
            else: # 이전에 누적 주차시간이 없으면
                total_time[car_number] = acc_time # 누적 주차시간 저장하기

    for car_number, time in records_dict.items():
        if flag_dict[car_number]: # 아직 출차 안한 차가 있으면
            acc_time = time_to_minute("23:59") - time # 23:59분에 출차 처리해주기, 누적 시간 계산
            # print(car_number, "23:59에 출차!", acc_time)
            records_dict[car_number] = 0
            if car_number in total_time:
                total_time[car_number] += acc_time
            else:
                total_time[car_number] = acc_time

    for car_number, acc_time in total_time.items():
        if acc_time > fees[0]: # 누적 주차시간이 기본 주차시간보다 길면
            total_cost.append((car_number, (fees[1] + ceil((acc_time - fees[0]) / fees[2]) * fees[3]))) # 요금 계산해서 청구
        else: # 누적 주차시간이 기본 주차시간 보다 짧으면
            total_cost.append((car_number, fees[1])) # 기본 요금만 청구

    total_cost.sort() # 차량 번호 오름차순 정렬
    result = []
    for cost in total_cost:
        result.append(cost[1]) # 비용만 result에 담기
    return result

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])