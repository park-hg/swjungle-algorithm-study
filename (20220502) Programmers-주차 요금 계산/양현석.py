import math

def solution(fees, records):
    answer = []
    dic = {}
    fee_list = {}
    for info in records:
        time, carNum, arrow = map(str, info.split(" "))
        total = 0
        if arrow == "IN":
            i_hour, i_min = time.split(":")
            i_total = int(i_hour)*60 +int(i_min)
            dic[carNum] = i_total
        else :                        #out이 나왔다는 것은 빼주면대
            o_hour, o_min = time.split(":")
            o_total = int(o_hour)*60 +int(o_min)
            total = o_total - dic[carNum]           #여기서 가격계산
            if carNum not in fee_list:
                fee_list[carNum] = total
                dic.pop(carNum)
            else:
                fee_list[carNum] += total
                dic.pop(carNum)
    
    last_time = 23*60 + 59
    
    for carNum, time in dic.items():
        
        if carNum in fee_list:
            fee_list[carNum] += last_time - time
        else:
            fee_list[carNum] = last_time - time
    
   
    sort_list = sorted(fee_list.items())
    
    # print(sort_list)
    for key, value in sort_list :
        # print(key,",",value)
        if value <= fees[0]:
            answer.append(fees[1])
            continue
        temp = math.ceil((value-fees[0])/fees[2])
        answer.append(fees[1] + temp*fees[3])
        
    
    return answer