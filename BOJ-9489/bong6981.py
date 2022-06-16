import sys
from traceback import print_tb
input = sys.stdin.readline

import heapq
from collections import defaultdict, deque

while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    nums = list(map(int, input().split()))


    parent = [nums[0]]

    lev_info = defaultdict(int)
    parent_info = defaultdict(int)
    child_info = defaultdict(list)

    lev_info[nums[0]] = 0
    parent_info[nums[0]] = 0
    child_info[nums[0]] = []

    tmp = deque([])
    prev = nums[0]

    for num in nums[1:]:
        if num == (prev)+1:
            tmp.append(num)
        else:
            if tmp:
                p = heapq.heappop(parent)
                print("p!! :", p)
                print(tmp)
                ttmp = []
                while tmp:
                    n = tmp.popleft()
                    parent_lev = lev_info[p]
                    child_info[p].append(n)
                    lev_info[n] = parent_lev+1
                    parent_info[n] = p
                    ttmp.append(n)
                for t in ttmp:
                    heapq.heappush(parent, t)
            tmp = deque()
            tmp.append(num)
        prev = num
    
    if tmp:
        p = heapq.heappop(parent)
        while tmp:
            n = tmp.popleft()
            parent_lev = lev_info[p]
            child_info[p].append(n)
            lev_info[n] = parent_lev+1
            parent_info[n] = p
            ttmp.append(n)

    print(lev_info)
    print(child_info)
    print(parent_info)
    ans = 0
    p = parent_info[K]
    print(p)
    if p != 0:
        grand = parent_info[p]
        print(grand)
        if grand != 0:
            print(child_info[grand])
            for ps in child_info[grand]:
                if ps == p:
                    continue
                else:
                    ans += len(child_info[ps])
    
    print(ans)

