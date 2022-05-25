from itertools import combinations

def solution(relation):
    answer = 0
    data_len = len(relation[0])
    database = [[] for _ in range(data_len * (data_len - 1) // 2)]
    check = {}
    is_key = [False for _ in range(data_len)]
    key_count = 0

    for k, rel in enumerate(relation):
        for n in range(1, data_len + 1):
            result = combinations(rel, n);
            for r in result:
                if r in database[n]:
                    check[(k, n)] = False
                else:
                    check[(k, n)] = True
                    database[n].append(r)
    for key, value in check.items():
        if value:
            print(key, value)
    print(database)
    print(check)
    
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])