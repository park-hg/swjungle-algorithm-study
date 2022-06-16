def solution(n, t, m, timetable):
  times = []
  for time in timetable:
    hh, mm = time.split(':')
    times.append(int(hh) * 60 + int(mm))
  times.sort()

  buses = []
  bus_time = 9 * 60
  for _ in range(n):
    buses.append(bus_time)
    bus_time += t
    
  answer = 0
  idx = 0
  for bus in buses:
    cnt = 0
    while cnt < m and idx < len(times) and times[idx] <= bus:
      cnt += 1
      idx += 1
    if cnt < m:
      answer = bus
    else:
      answer = times[idx - 1] - 1
    

  answer_hh = answer // 60
  answer_mm = answer - answer_hh * 60
  print(str(answer_hh).zfill(2) + ':' + str(answer_mm).zfill(2))
    
  return str(answer_hh).zfill(2) + ':' + str(answer_mm).zfill(2)
