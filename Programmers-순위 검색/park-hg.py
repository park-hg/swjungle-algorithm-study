import bisect
from collections import defaultdict

def solution(info, query):
    d = defaultdict(list)
    info = [x.split() for x in info]
    for i in info:
        for bit in range(1<<4):
            key = i[:-1][:]
            for j in range(4):
                if bit & (1<<j):
                    key[j] = '-'
            d[tuple(key)].append(int(i[-1]))
    
    for key in d:
        d[key].sort()
    
    ans = []
    for q in query:
        q = q.replace(' and ',' ')
        q = q.split()
        score = int(q[-1])
        idx = bisect.bisect_left(d[tuple(q[:-1])], score)
        ans.append(len(d[tuple(q[:-1])]) - idx)
        
    return ans