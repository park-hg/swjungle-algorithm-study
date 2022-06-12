
# 셔틀은 9:00 부터 총 n회 t분 간격으로 역에 도착하며 하나의 셔틀에넌 최대 m명의 승객이 탈 수 있다
# 9:00에 줄선 크루원도 탈 수 있고
# 사무실에 도착하는 제일 늦은 시각
# 모든 크루는 23:59에 집에 돌아간다
# 셔틀을 타고 집에는 가야지 59분에는 와야 탈수 있으니까
# 만약 버스가 안남아 있다(남은 자리도 없다) -> 내가 앞시간에 무조건 타야해
# 버스 안남아있고, 자리 여유롭다? 그 숫자에서 맨 마지막에는 타야해
# 버스 남아있으면 여유롭게 타도돼?
# 3번 태케가 9시에는 8시애만 타니까 9시 9분에는 타야 내가 탈수있네

# 버스가 몇대 운행하는지, 몇분 간격으로 운행하는지, 수용인원이 얼마인지, 몇시몇분에 대기타고 있는지

# 9시에 시작해서 간격(t)마다 n을 빼줘 그리고 시간 된 애들 보내줘
# n == 1 일때는 내가 무조건 가야하니까 그걸 계산해줘

from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    time_list = []
    temp = 0
    startTime = 9*60
    
    for time in timetable :
        hour , mint = time.split(":")
        total = int(hour) * 60 + int(mint)
        time_list.append(total)
    
    q = deque()
    time_list.sort()
    q = deque(time_list)
 
    while n >= 1 :
        
        if n == 1 :      
            if m > len(q) :
                temp = startTime
            else:
                tt = m
                while tt >= 1 :
                    now = q[0]
                    if now <= startTime :
                        q.popleft()
                        temp = now - 1
                        tt -=1
                    else:
                        temp = startTime
                        break
                    
            break  # n == 1일 때는 무조건 타야하므로
  
        cnt = 0
    
        while q :  
            now = q[0]
            cnt += 1
            if startTime >= now : 
                q.popleft()
  
            if cnt == m :    #다 찼으면 n 빼주고 다음 while문
                startTime += t
                n -=1
                break
                         
        else:
            temp = startTime
            break
             
     
    hour = temp // 60
    mintus = temp - (hour * 60)
    str_hour = str(hour)
    str_min = str(mintus)
    if len(str_hour) == 1 :
        str_hour = "0" + str_hour
    if len(str_min) == 1 :
        str_min = "0" + str_min
    answer = str_hour + ":" + str_min
    
    return answer