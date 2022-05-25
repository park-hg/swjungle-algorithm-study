from itertools import combinations, permutations
from collections import defaultdict

def check(cand, key, relation):
    if cand in key:
        return False
    
    for i in range(1, len(cand)+1):
        for p in permutations(list(cand), i):
            if tuple(p) in key:
                return False
    
    include_all = set()
    for r in relation:
        data = []
        for i in list(cand):
            data.append(r[i])
        data = tuple(data)
        if data in include_all:
            return False
    print(include_all)
    return True

def solution(relation):
    ## 각각 항목 별로 set에 담아서 항목을 set에 담고, (idx), 항목별로 set에 담아 
    ## 1~n(요소의 개수만큼 combination)해서 set으로 해서 전체 개수가 되면은 그 집합을 빼야 한다. 
    answer = 0
    ele_cnt = len(relation[0])
    arr = [i for i in range(ele_cnt)]
    
    # set_relation = [defaultdict(set) for _ in range(ele_cnt)]
    # for idx, r in enumerate(relation):
    #     for i in range(ele_cnt):
    #         ele = r[i]
    #         set_relation[i][ele].add(idx)

    # print(set_relation)

    answer = 0
    key = set()
    for i in range(1, ele_cnt+1):
        for cb in combinations(arr, i):
            cb = tuple(sorted(cb))
            if check(cb, key, relation):
                print(cb)
                answer += 1
                key.add(cb)
    
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


