def int_to_time(number):
    hh = number//60
    if hh < 10:
        hh = "0"+str(hh)
    else :
        hh = str(hh)

    mm = number%60
    if mm < 10:
        mm = "0"+str(mm)
    else :
        mm = str(mm)

    time = hh+":"+mm
    return time

def time_to_int(time):
    hh, mm = time.split(":")
    number = int(hh)*60+int(mm)
    return number

def solution(n, t, m, timetable):
    sort_table = []
    answer = 0
    last = 0
    bus = 540
    length = len(timetable)
    remain = 0

    for i in timetable:
        sort_table.append(time_to_int(i))
    sort_table.sort()

    for i in range(n):
        for j in range(m):
            now = sort_table[last]
            if now <= bus:
                last += 1
                if last == length:
                    break
            else :
                remain += m-j
                break
        
        bus += t
        if last == length:
            break
    
    if last == n*m :
        answer = int_to_time(sort_table[last-1]-1)    
    else :
        if length - last == 0:
            answer = int_to_time(sort_table[last-1]-1)
        else :
            if sort_table[last] <= 540+(n-1)*t:
                answer = int_to_time(sort_table[last-1]-1)
            else :   
                answer = int_to_time(540+(n-1)*t)
    return answer


# nn = 2
# tt = 1
# mm = 2
# table = ["09:00", "09:00", "09:00", "09:00"]

# print(solution(nn,tt,mm,table))

# nn = 2
# tt = 10
# mm = 2
# table =	["09:10", "09:09", "08:00"]

# print(solution(nn,tt,mm,table))

# nn = 1	
# tt = 1
# mm = 5
# table = ["08:00", "08:01", "08:02", "08:03"]

# print(solution(nn,tt,mm,table))

nn = 10	
tt = 60
mm = 45	
table = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

print(solution(nn,tt,mm,table))

nn = 1
tt = 1
mm = 1
table =	["23:59"]

print(solution(nn,tt,mm,table))