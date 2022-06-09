from heapq import *
from collections import deque
def solution(jobs):
    n = len(jobs)
    jobs.sort()
    jobs = deque(jobs)
    cur_time = jobs[0][0]
    answer = 0
    heap = []

    while jobs:
        while jobs and jobs[0][0] <= cur_time:
            job = jobs.popleft()
            heappush(heap, (cur_time+job[1], job))

        if heap:
            next_time, next_job = heappop(heap)
            answer += next_time - next_job[0]
            cur_time = next_time
            while heap:
                _, next_job = heappop(heap)
                jobs.appendleft(next_job)
        else:
            cur_time = jobs[0][0]

    return answer/n


print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))