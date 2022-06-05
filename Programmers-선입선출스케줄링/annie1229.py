def solution(n, cores):
    answer = 0
    start = 0
    end = n * max(cores)
    check_time = 0
    check_count = 0
    
    while start <= end:
      mid = (start + end) // 2
      count = 0
      for core in cores:
        count += mid // core
      if count < n - len(cores):
        check_time = mid
        check_count = count
        start = mid + 1
      else:
        end = mid - 1
      # print('mid', mid, 'count', count, 'check', check_time, 'check_count', check_count)

    left = n - len(cores) - check_count
    
    for idx, core in enumerate(cores):
      if (check_time + 1) % core == 0:
        left -= 1
        if left == 0:
          answer = idx + 1

    # print('answer', answer)
    return answer


solution(6, [1, 2, 3])