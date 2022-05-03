
def solution(fees, records):
    records = sorted(records, key = lambda x:x[1])
    time =[0]*1001
    money = [0]*1001
    carnum = []
    answer = []


    for i in range(len(records)):

        info = list(map(str, records[i].split(" ")))

        idx = 1001
        if info[2] == "IN":
            if info[1] in carnum:
                idx = carnum.index(info[1])
            else :
                time.append(info[1])
                idx = len(carnum)-1
        
            time[idx] = info[0]
        
        else:
            idx = carnum.index(info[1])
            in_hour, in_min = int(time[idx].split(":"))
            out_hour, out_min = int(info[0].split(":"))
            
            in_time = in_hour*60 + in_min
            out_time = out_hour*60 + out_min

            total = out_time-in_time
            fee = 0
            if total <=300:
                fee = 5000
            else :
                fee = 5000 + ((total-300)//10)*600

            money[idx] += fee
            time[idx] = 0

    return answer


fees = [180, 5000, 10, 600]
record = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]