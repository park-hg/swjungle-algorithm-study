# HH:MM 형식으로 들어온 입차시간, 출차시간을 가지고
# (출차시간 - 입차시간)의 결과값을 분으로 변환하는 함수
def get_min_from_hhmm(in_hhmm, out_hhmm):
  in_hh, in_mm = in_hhmm.split(':')
  out_hh, out_mm = out_hhmm.split(':')

  result = 0
  result += int(out_hh) * 60
  result += int(out_mm)
  result -= int(in_hh) * 60
  result -= int(in_mm)

  return result

  
# 총 시간(분)으로 주차요금을 계산하는 함수
def get_fee(total_minutes, fees):
  if total_minutes <= fees[0]:
    return fees[1]
  else:
    result = 0
    total_minutes -= fees[0]
    result += fees[1]
    if total_minutes % fees[2] == 0:
      result += ((total_minutes // fees[2])) * fees[3]
    else:
      result += ((total_minutes // fees[2]) + 1) * fees[3]
    return result
  

def solution(fees, records):
  cars = {}
  for record in records:
    time, car_num, in_out = record.split()
    if car_num in cars:
      cars[car_num].append(time)
    else:
      cars[car_num] = [time]

  result = []
  for car_num in cars:
    if len(cars[car_num]) % 2 == 1: # 입차된 후 출차 내역이 없는 경우
      cars[car_num].append("23:59") # 23:59에 출차되었다고 간주
      
    car_total_time = 0
    for i in range(0, len(cars[car_num]), 2):
      car_total_time += get_min_from_hhmm(cars[car_num][i], cars[car_num][i+1])

    car_fee = get_fee(car_total_time, fees)
    result.append((car_num, car_fee))

  result.sort()
  answer = []

  #출력형식에 맞게 변환
  for i in range(len(result)):
    answer.append(result[i][1])
  return answer
